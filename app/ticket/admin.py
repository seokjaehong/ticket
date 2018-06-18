from django.contrib import admin

# Register your models here.
# from ticket.models.ticketdata import *
from ticket.models.ticketdata import TicketData
from .models import *

admin.site.register(TicketData)