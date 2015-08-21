from django.contrib import admin
from app import models

# Register your models here.
class MailAdmin(admin.ModelAdmin):
    exclude = ('created', )
    list_display = ('first_name', 'last_name', 'email_to', 'email_from')
    list_display_links = ('first_name', 'last_name',)
    list_filter = ('owner',)
    search_fields = ['first_name', 'last_name', 'email_to', 'email_from']

admin.site.register(models.Mail, MailAdmin)
