from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template import RequestContext

from crawler.expedia import get_ticket_information
from search_flight.models import City_Infomation, TicketInfomation

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_flight(request):
    pass


#     if request.method == 'POST':
#         startcity = request.POST['startcity']
#         arrivecity = request.POST['arrivecity']
#         startdate = request.POST['startdate']
#         enddate = request.POST['enddate']
#         price = request.POST['price']
#         print(startcity,arrivecity,startdate,enddate,price)
#
#
#         # db저장할 때
#
#
#         # ticket, _ = TicketInfomation.objects.get_or_create(
#         #     startcity=info[0]['startcity'],
#         #     arrivecity=info[0]['endcity'],
#         #     startdate=info[0]['stardate'],
#         #     enddate=info[0]['enddate'],
#         #     price=info[0]['price'],
#         # )
#
#         return HttpResponse(info)


@csrf_exempt
def SearchFlight(request):
    context = dict()

    city = City_Infomation.objects.all()

    if request.method == 'POST':

        startcity_info = request.POST['startcity']
        arrivecity_info = request.POST['arrivecity']

        startdate_info = request.POST['startdate']
        enddate_info = request.POST['enddate']
        price_info = request.POST['price']

        startcity = City_Infomation.objects.get(pk=startcity_info).get_cityname_display()
        arrivecity = City_Infomation.objects.get(pk=arrivecity_info).get_cityname_display()

        result = get_ticket_information(startdate_info, enddate_info, startcity, arrivecity)

        start = result[0]
        arrive = result[1]

        print(start['출발']['time'])
        price = start['출발']['price'] + arrive['도착']['price']

        if int(price_info) >= price:
            startdate = datetime.strptime(startdate_info, '%Y.%m.%d')
            enddate = datetime.strptime(enddate_info, '%Y.%m.%d')
            ticket, _ = TicketInfomation.objects.get_or_create(
                startcity=City_Infomation.objects.get(pk=startcity_info),
                arrivecity=City_Infomation.objects.get(pk=arrivecity_info),
                startdate=startdate,
                enddate=enddate,
                price=price,
            )

            context['start_time'] = start['출발']['time']
            context['arrive_time'] = arrive['도착']['time']
            context['price'] = price
            return render(request, 'index.html', context)

    context['items'] = city
    return render_to_response('index.html', context)
