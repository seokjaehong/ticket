from rest_framework import serializers
from rest_framework.utils.field_mapping import get_nested_relation_kwargs

from mail.models import SelectedTicket, Receiver
from ticket.models.ticketdata import TicketData


class TicketInformationSerializer(serializers.ModelSerializer):
    max_price = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()

    class Meta:
        model = TicketData

        fields = (
            'id',
            'ticket_price',
            'departure_date',
            'departure_datetime',
            'origin_place',
            'destination_place',
            'ticket_price',
            'max_price',
            'receiver'
        )

    def get_max_price(self, obj):
        return self.context["user_max_price"] - obj.ticket_price

    def get_receiver(self, obj):
        return obj.receivers.first().receiver.mail_address


class ReceiverInformationSerializer(serializers.ModelSerializer):
    ticket_lists = serializers.SerializerMethodField()

    class Meta:
        model = Receiver
        fields = (
            'id',
            'mail_address',
            'user_max_price',
            'ticket_lists',
        )

        # order_by = ['-created']

    def get_ticket_lists(self, obj):

        if self.context['a']:
            print('높은 값순')
            tickets = obj.ticket_lists.all().order_by('-ticket_price')
        else:
            print('낮은 값순')
            tickets = obj.ticket_lists.all().order_by('ticket_price')
        max_price = obj.user_max_price
        serializer = TicketInformationSerializer(tickets, context={"user_max_price": max_price}, many=True)
        return serializer.data

    # def get_context(self):
    #     return self.context
