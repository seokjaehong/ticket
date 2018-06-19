from django.contrib import admin

# Register your models here.
from .models.mail_condition import MailCondition
from .models.ticketdata import TicketData


admin.site.register(TicketData)
admin.site.register(MailCondition)