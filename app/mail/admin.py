from django.contrib import admin

# Register your models here.
from mail.models import Receiver, SelectedTicket


class ReceiverAdmin(admin.ModelAdmin):
    search_fields = ('mail_address',)
    list_filter = ("origin_place",)
    list_display = ('mail_address','user_max_price',)

class SelectedTicketAdmin(admin.ModelAdmin):
    filter_horizontal = ('receiver',)
    


admin.site.register(Receiver, ReceiverAdmin)
admin.site.register(SelectedTicket)
