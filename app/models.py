from django.db import models

# Create your models here.

class Mail(models.Model):
    owner = models.ForeignKey('auth.User', related_name='mails', default=0)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_from = models.EmailField()
    email_to = models.EmailField()
    message = models.TextField()
    host_ip = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)
