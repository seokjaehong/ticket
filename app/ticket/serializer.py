from rest_framework import serializers

from mail.models import SelectedTicket, Receiver
from ticket.models.ticketdata import TicketData


class TicketInformationSerializer(serializers.ModelSerializer):
    dif_value = serializers.SerializerMethodField()

    # def __init__(self, *args, **kwargs):
    #     super(serializers.ModelSerializer, self).__init__(*args, **kwargs)
    #     print("# -1")
    #     print(args)
    #     print(kwargs)
    #     self.context["user_max_price"] = kwargs["context"]["user_max_price"]
        # super(serializers.ModelSerializer, self).__init__(*args, **kwargs)
    # def get_context(self):
    #     print('1212111212121')
    #     return self.context

    def get_dif_value(self, obj):

        receivers =self.context['receivers']
        # print(recei)
        # ticket = obj.receivers.first()
        # print(ticket)
        # receiver=receivers.filter(ticket_lists=obj)
        # print(obj)
        # return receiver.user_max_price - obj.ticket_price
        return 0

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
    def get_context(self):
        return self.context
    # user_max_price = serializers.SerializerMethodField()
    ticket_lists = TicketInformationSerializer(context=get_context, many=True)

    class Meta:
        model = Receiver
        fields = (
            'id',
            'mail_address',
            'user_max_price',
            'ticket_lists',
        )

    # def get_user_max_price(self, obj):
    #     print("# 0")
    #     print(obj)
    #     obj.aaa = '123456'
    #     return obj.user_max_price
