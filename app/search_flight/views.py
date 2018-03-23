from datetime import datetime

from django.shortcuts import render, get_object_or_404, render_to_response

# Create your views here.
from django.template import RequestContext

from crawler.expedia import get_ticket_information
from search_flight.models import City_Infomation


def SearchFlight(request):
    context = dict()

    city = City_Infomation.objects.all()
    if request.method == 'POST':

        startcity = request.POST['startcity']
        arrivecity = request.POST['arrivecity']
        startdate_info = request.POST['startdate']
        enddate_info = request.POST['enddate']
        price_info = request.POST['price']

        print(startcity, arrivecity)

        stardate = datetime.strptime(startdate_info, '%Y.%m.%d')
        enddate = datetime.strptime(enddate_info, '%Y.%m.%d')

        result = get_ticket_information(startdate_info, enddate_info, 'SEL', 'PUS')

        start = result[0]
        arrive = result[1]

        price = start['출발']['price'] + arrive['도착']['price']

        if int(price_info) >= price:
            context['result'] = result
            return render(request, 'index.html', context)

    context['items'] = city
    # return render(request, 'index.html', {'items': city})
    return render_to_response('index.html', context)
    # return render(request,'index.html')
