from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from mail.models import SelectedTicket, Receiver
from ticket.serializer import ReceiverInformationSerializer


# class TicketInformationView(APIView):
#
#     def get(self, request, format=None):
#         selected_tickets = SelectedTicket.objects.all()
#         serializer = SelectedTicketInformationSerializer(selected_tickets, many=True)
#
#         return Response(serializer.data, status=status.HTTP_200_OK)

class ReceiverInformationView(APIView):
    def get(self, request, format=None):
        try:

            receivers = Receiver.objects.all()

            serializer = ReceiverInformationSerializer(receivers, context={'receivers':receivers}, many=True)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)
