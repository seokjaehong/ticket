from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from mail.models import SelectedTicket, Receiver
from ticket.serializer import ReceiverInformationSerializer


class ReceiverInformationView(APIView):

    def get(self, request, *args, **kwargs):
        try:
            # sort = self.kwargs['sort_by']
            # a = self.request.query_params.get('sort_by')
            a = request.META.get('HTTP_SORT_BY')
            print(a)
            # print(sort)
            receivers = Receiver.objects.all()
            context = {'a': a}
            serializer = ReceiverInformationSerializer(receivers, context=context, many=True)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_200_OK)
