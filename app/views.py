from django.shortcuts import render

# Create your views here.
import smtplib
import datetime
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
from webservices.settings import EMAIL_TO, EMAIL_SUBJECT

@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'mails': reverse('mail-list', request=request, format=format)
    })

class UserViewSet(viewsets.ModelViewSet):
    """
    List of all api users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permissions_classes = (permissions.IsAdminUser,)

class MailViewSet(viewsets.ModelViewSet):
    """
    To get all sent mails and send mail to admin mail-id
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
            send_mail(EMAIL_SUBJECT, self.request.data['message'], self.request.data['email_from'], [EMAIL_TO])
        except smtplib.SMTPException:
            raise MailServiceUnavailable
        serializer.save(owner=self.request.user, email_to=EMAIL_TO, host_ip=self.request.META['REMOTE_ADDR'])

def error404(request):
    """
    Custom 404 Json Reponse
    """
    data = {
    "status_code" : 404,
    "error" : "The resource was not found"
    }
    return JsonResponse(data)
