from datetime import datetime, date

from django.shortcuts import render

# from crawler.jeju import JejuData
from crawler.utils import get_ticket_information_single_date
from ticket.tasks import get_ticket_information_save

__all__ = (
    'ticket_search_from_jeju',
)


def ticket_search_from_jeju(request):
    departure_date = request.GET.get('departure_date')
    # air_route = str(request.GET.get('air_route'))
    # origin_place = air_route[:3]
    # destination_place = air_route[4:]

    tickets = []

    if departure_date:
        from ticket.models.ticketdata import TicketData
        datetime_departure_date = date(*(int(s) for s in departure_date.split('-')))

        get_ticket_information_save.delay(datetime_departure_date, 'TW')
        get_ticket_information_save.delay(datetime_departure_date, 'LJ')
        get_ticket_information_save.delay(datetime_departure_date, 'KE')
        get_ticket_information_save.delay(datetime_departure_date, 'OZ')
        get_ticket_information_save.delay(datetime_departure_date, 'BX')
        get_ticket_information_save.delay(datetime_departure_date, '7C')
        get_ticket_information_save.delay(datetime_departure_date, 'ZE')
        tickets = TicketData.objects.filter(departure_date=datetime.strptime(departure_date, "%Y-%m-%d"))
                                            # origin_place=origin_place, destination_place=destination_place)

    context = {'tickets': tickets}
    return render(request, 'ticket/search_from_webpage.html', context)
