import feedparser
import twitter
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from rest_framework import authentication, permissions, status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.reverse import reverse

from app.serializers import MailSerializer
from app.utils import get_readable_date, get_summary


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    """
    Return a list of all available endpoints
    """
    return Response(
        {
            "mails": reverse("send-mail", request=request, format=format),
            "tweets": reverse("tweet-list", request=request, format=format),
            "blogs": reverse("blog-list", request=request, format=format),
        },
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@authentication_classes((authentication.TokenAuthentication,))
@permission_classes((permissions.IsAuthenticated,))
def send_mail(request, format=None):
    """
    Send mail to admin
    """
    # serialize request data
    serializer = MailSerializer(data=request.data)

    if serializer.is_valid():
        try:
            # create data for mail
            subject = settings.EMAIL_SUBJECT.format(
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
            )
            msg = request.data["message"]
            email_from = request.data["email_from"]

            # send mail
            EmailMessage(subject, msg, email_from, [settings.EMAIL_TO]).send()

            # save mail instance
            serializer.save(
                owner=request.user,
                email_to=settings.EMAIL_TO,
                host_ip=request.META["REMOTE_ADDR"],
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception:
            pass

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_tweets(request, format=None):
    """
    To get the latest tweets from admin profile
    """
    count = None
    if "count" in request.query_params:
        count = request.query_params["count"]
    api = twitter.Api(
        consumer_key=settings.TWITTER_CONSUMER_KEY,
        consumer_secret=settings.TWITTER_CONSUMER_SECRET,
        access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
        access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET,
    )
    tweets = api.GetUserTimeline(screen_name=settings.TWITTER_SCREEN_NAME, count=count)
    data = []
    for tweet in tweets:
        data.append(
            {"id": tweet.id, "created_at": tweet.created_at, "text": tweet.text}
        )
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def get_blogs(request, format=None):
    """
    To get blog list from rss feed
    """
    # get raw parsed data of RSS feed
    raw_data = feedparser.parse(settings.RSS_FEED_URL)
    # feed = raw_data['feed']

    # append each blog entry to result data
    data = []
    for entry in raw_data["entries"]:
        data.append(
            {
                "title": entry["title"],
                "author": entry["author"],
                "link": entry["link"],
                "summary": {
                    "plaintext": get_summary(entry["summary"]),
                    "html": entry["summary"],
                },
                "updated_date": get_readable_date(entry["updated"]),
            }
        )

    return Response(data, status=status.HTTP_200_OK)


def error404(request, exception):
    """
    Custom 404 Json Reponse
    """
    data = {"status_code": 404, "error": "The resource was not found"}
    return JsonResponse(data)
