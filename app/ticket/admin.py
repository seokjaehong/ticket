from django.contrib import admin

# Register your models here.
from .models.ticketdata import TicketData


admin.site.register(TicketData)