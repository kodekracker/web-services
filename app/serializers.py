from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Mail


class MailSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    email_to = serializers.ReadOnlyField()
    host_ip = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = Mail
        fields = ('id', 'owner', 'first_name', 'last_name', 'email_from', 'email_to', 'message', 'host_ip', 'created' )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    mails = serializers.HyperlinkedRelatedField(many=True, view_name='mail-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'mails')


