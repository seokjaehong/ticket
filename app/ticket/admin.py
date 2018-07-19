from django.contrib import admin

# Register your models here.
from django.contrib.admin import DateFieldListFilter

from .models.ticketdata import TicketData


class TicketAdmin(admin.ModelAdmin):
    list_filter = (
        'origin_place',
        'destination_place',
        ('departure_date', DateFieldListFilter),
        ('arrival_date', DateFieldListFilter)
    )
    search_fields = (
        'origin_place',
        'destination_place',
        'departure_date',
        'arrival_date',
    )


admin.site.register(TicketData, TicketAdmin)
