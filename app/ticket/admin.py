from django.contrib import admin

# Register your models here.
from .models.mail_history import MailHistory
from .models.ticketdata import TicketData


admin.site.register(TicketData)
admin.site.register(MailHistory)