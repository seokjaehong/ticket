from django.contrib import admin

# Register your models here.
from mail.models import Receiver,SelectedTicket

admin.site.register(Receiver)
admin.site.register(SelectedTicket)