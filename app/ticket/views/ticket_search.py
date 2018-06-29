from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from ticket.models.ticketdata import TicketData

__all__ = (
    'ticket_search',
)


def ticket_search(request):
    """
     Template: ticket/ticket_search.html
        form (input[departure_date], 조회 button 한 개)
    1. form에 주어진 'departure date'로 database의 검색 결과를 보여줌
    2.
    :param request:
    :return:
    """

    departure_date = request.GET.get('departuredate')
    tickets = []
    if departure_date:
        tickets = TicketData.objects.filter(departure_date=datetime.strptime(departure_date, "%Y-%m-%d"))
    context = {'tickets': tickets}
    return render(request, 'ticket/search.html', context)
