from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class Mail(models.Model):
    # Attributes
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_from = models.EmailField()
    email_to = models.EmailField()
    message = models.TextField()
    host_ip = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)

    # Relations
    owner = models.ForeignKey('auth.User', related_name='mails',
                              on_delete=models.CASCADE)

    # Functions
    def __repr__(self):
        return _('%s %s %s') % (self.first_name, self.email_from,
                                self.email_to)

    # Meta
    class Meta:
        ordering = ('created',)
