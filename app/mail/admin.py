from django.contrib import admin

# Register your models here.
from mail.models import Receiver

admin.site.register(Receiver)