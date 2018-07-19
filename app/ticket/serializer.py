from rest_framework import serializers

from mail.models import SelectedTicket, Receiver
from ticket.models.ticketdata import TicketData


class TicketInformationSerializer(serializers.ModelSerializer):
    dif_value = serializers.SerializerMethodField()

    # def get_context(self):
    #     print('1212111212121')
    #     return self.context

    def get_dif_value(self, obj):
        # ticket= TicketData.objects.all()
        max = obj.receivers.first().receiver.user_max_price
        # print(self.get_context()['context'])
        return max - obj.ticket_price

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
            'dif_value',
        )


class ReceiverInformationSerializer(serializers.ModelSerializer):
    receiver = Receiver.objects.all()
    # user_max_price = serializers.SerializerMethodField
    ticket_lists = TicketInformationSerializer(context={'user_max_price': receiver}, many=True)

    class Meta:
        model = Receiver
        fields = (
            'id',
            'mail_address',
            'user_max_price',
            'ticket_lists',
        )
    #
    # def get_user_max_price(self):
    #     return self.user_max_price