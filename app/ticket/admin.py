from django.contrib import admin

# Register your models here.
from .models.ticketdata import TicketData


class TicketAdmin(admin.ModelAdmin):
    list_filter = ('origin_place', 'destination_place', 'departure_datetime', 'arrival_datetime',)
    search_fields = ('origin_place','destination_place', 'departure_datetime', 'arrival_datetime',)


admin.site.register(TicketData, TicketAdmin)
