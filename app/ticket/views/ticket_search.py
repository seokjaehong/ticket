from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

from ticket.models.ticketdata import TicketData

__all__ = (
    'ticket_search',
)


def ticket_search(request):
    """
     Template: ticket/ticket_search_from_site.html
        form (input[year,month,date=keyword], 세개, button한 개)
    1. form에 주어진 'keyword'로 티웨이 항공사이트의 티켓 검색 결과를 크롤링,,

    :param request:
    :return:
    """

    departuredate= request.GET.get('departuredate')
    print(departuredate)

    departuredate = datetime.strptime(departuredate, "%Y-%m-%d")

    tickets = TicketData.objects.filter(departure_date=departuredate)
    print(tickets)
    # tickets = TicketData.objects.all()
    context = {
        'tickets': tickets,
    }
    return render(
        request,
        'ticket/search.html',
        # 'artist:artist-list',
        context,
    )

    # return HttpResponse('hello')
    # return render(request, 'artist/artist_search_from_melon.html', context)
