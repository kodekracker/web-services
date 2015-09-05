from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from app.views import api_root, send_mail, get_tweets, get_blogs

urlpatterns = [
    url(r'^api/auth-token/$', obtain_auth_token, name="get-auth-token"),
    url(r'^api/mails/$', send_mail, name='send-mail'),
    url(r'^api/tweets/$', get_tweets, name='tweet-list'),
    url(r'^api/blogs/$', get_blogs, name='blog-list'),
    url(r'^$', api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
