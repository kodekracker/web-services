from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from app.views import MailViewSet, api_root, get_tweets

mail_list = MailViewSet.as_view({
    'post': 'create'
    })

urlpatterns = [
    url(r'^api/auth-token/$', obtain_auth_token, name="get-auth-token"),
    url(r'^api/mails/$', mail_list, name='mail-list'),
    url(r'^api/tweets/$', get_tweets, name='tweet-list'),
    url(r'^$', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
