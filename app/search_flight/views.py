from datetime import datetime

from django.shortcuts import render

# Create your views here.
from crawler.expedia import get_ticket_information


def SearchFlight(request):
    context = dict()

    if request.method == 'POST':
        startcity = request.POST['startcity']
        arrivecity = request.POST['arrivecity']
        startdate_info = request.POST['startdate']
        enddate_info = request.POST['enddate']
        price_info = request.POST['price']

        stardate = datetime.strptime(startdate_info, '%Y.%m.%d')
        enddate = datetime.strptime(enddate_info, '%Y.%m.%d')

        result = get_ticket_information(startdate_info, enddate_info, 'SEL', 'PUS')

        start = result[0]
        arrive = result[1]

        price = start['출발']['price'] + arrive['도착']['price']

        if int(price_info) >= price:
            context['result'] = result
            return render(request, 'index.html', context)

    return render(request, 'index.html')
