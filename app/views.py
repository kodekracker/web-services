from django.shortcuts import render

# Create your views here.
import twitter
import smtplib
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from app.models import Mail
from app.serializers import MailSerializer, UserSerializer
from app.utils import MailServiceUnavailable

@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'mails': reverse('mail-list', request=request, format=format),
        'tweets': reverse('tweet-list', request=request, format=format)
    })

class MailViewSet(viewsets.ModelViewSet):
    """
    To send mail to admin through mailgun SMTP server
    """
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view should return a list of all the mails
        for the currently authenticated user.
        """
        user = self.request.user
        return Mail.objects.filter(owner=user)

    def perform_create(self, serializer):
        """
        This view should sent a mail to admin and also store information
        in the database
        """
        # send mail to mailgun server
        try:
            send_mail(setttings.EMAIL_SUBJECT, self.request.data['message'],
                self.request.data['email_from'], [settings.EMAIL_TO])
        except smtplib.SMTPException:
            raise MailServiceUnavailable
        serializer.save(owner=self.request.user, email_to=settings.EMAIL_TO,
            host_ip=self.request.META['REMOTE_ADDR'])

@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def get_tweets(request, format=None):
    """
    To get the lastest tweets from admin profile
    """
    count = None
    if 'count' in request.query_params:
        count=request.query_params['count']
    api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
    )
    tweets = api.GetUserTimeline(screen_name=settings.TWITTER_SCREEN_NAME,
        count=count)
    data = []
    for tweet in tweets:
        data.append({
            "id": tweet.id,
            "created_at": tweet.created_at,
            "text": tweet.text
            })
    return Response(data)

def error404(request):
    """
    Custom 404 Json Reponse
    """
    data = {
    "status_code" : 404,
    "error" : "The resource was not found"
    }
    return JsonResponse(data)
