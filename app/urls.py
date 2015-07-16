from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from app.views import UserViewSet, MailViewSet, api_root

user_list = UserViewSet.as_view({
    'get': 'list'
    })

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
    })

mail_list = MailViewSet.as_view({
    'get': 'list',
    'post': 'create'
    })

mail_detail = MailViewSet.as_view({
    'get': 'retrieve'
    })

urlpatterns = [
    url(r'^api/auth-token/$', obtain_auth_token, name="get-auth-token"),
    url(r'^api/users/$', user_list, name="user-list"),
    url(r'^api/users/(?P<pk>[0-9]+)/$', user_detail, name="user-detail"),
    url(r'^api/mails/$', mail_list, name='mail-list'),
    url(r'^api/mails/(?P<pk>[0-9]+)/$', mail_detail, name='mail-detail'),
    url(r'^$', api_root),
]
