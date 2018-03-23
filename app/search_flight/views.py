from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template import RequestContext

from crawler.expedia import get_ticket_information
from search_flight.models import City_Infomation

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_flight(request):
    if request.method == 'POST':
        info = request.POST['info']
        info[0]

        ticket, _ =  TicketInfomation.objects.get_or_create(

        )


        return HttpResponse(info)


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

        # db저장할 때
        startdate = datetime.strptime(startdate_info, '%Y.%m.%d')
        enddate = datetime.strptime(enddate_info, '%Y.%m.%d')

        result = get_ticket_information(startdate_info, enddate_info, startcity, arrivecity)

        start = result[0]
        arrive = result[1]

        print(start['출발']['time'])
        price = start['출발']['price'] + arrive['도착']['price']

        if int(price_info) >= price:
            info = list()
            info.append({
                'startcity': startcity,
                'endcity': arrivecity,
                'stardate': startdate,
                'enddate': enddate,
                'price': price,
            })

            context['info'] = info
            context['start_time'] = start['출발']['time']
            context['arrive_time'] = arrive['도착']['time']
            context['price'] = price
            return render(request, 'index.html', context)

    context['items'] = city
    return render_to_response('index.html', context)
