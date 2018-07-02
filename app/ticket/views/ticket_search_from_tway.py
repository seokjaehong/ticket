import datetime

from django.shortcuts import render

from crawler.twayair import TwayData

__all__ = (
    'ticket_search_from_tway',
)


def ticket_search_from_tway(request):
    """
     Template: ticket/ticket_search.html
        form (input[departure_date], 조회 button 한 개)
    1. form에 주어진 'departure date'로 tway항공에 대한 검색 결과를 저장하고 리스트를 전달
    :param request:
    :return:
    """
    departure_date = request.GET.get('departure_date')
    print(departure_date)
    add_days = 10
    tickets = []

    if departure_date:
        from ticket.models.ticketdata import TicketData
        crawler = TwayData()

        datetime_departure_date = datetime.date(*(int(s) for s in departure_date.split('-')))
        ticket_data_list = crawler.get_ticket_information(datetime_departure_date, add_days=add_days)

        for single_ticket_data in ticket_data_list:
            for ticket_data in single_ticket_data:
                obj, updated = TicketData.objects.update_or_create(
                    origin_place=ticket_data['origin_place'],
                    destination_place=ticket_data['destination_place'],
                    is_direct=ticket_data['is_direct'],
                    way_point=ticket_data['way_point'],
                    way_point_duration=ticket_data['way_point_duration'],
                    ticket_price=ticket_data['ticket_price'],
                    departure_date=ticket_data['departure_date'],
                    departure_datetime=ticket_data['departure_datetime'],
                    arrival_date=ticket_data['arrival_date'],
                    arrival_datetime=ticket_data['arrival_datetime'],
                    flight_time=ticket_data['flight_time'],
                    flight_company=ticket_data['flight_company'],
                    currency=ticket_data['currency'],
                    data_source=ticket_data['data_source'],
                    leftseat=ticket_data['leftseat'],
                )

        tickets = TicketData.objects.filter(departure_date=datetime.datetime.strptime(departure_date, "%Y-%m-%d"))

    context = {'tickets': tickets}
    return render(request, 'ticket/search_from_tway.html', context)
