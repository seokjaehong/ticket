from django.shortcuts import render

# Create your views here.
from crawler.expedia import get_ticket_information


def SearchFlight(request):
    context = dict()

    if request.method == 'POST':
        startcity = request.POST['startcity']
        arrivecity = request.POST['arrivecity']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        price_info = request.POST['price']

        result = get_ticket_information('2018.03.31', '2018.04.24', 'SEL', 'PUS')

        start = result[0]
        arrive = result[1]

        price = start['출발']['price'] + arrive['도착']['price']

        if int(price_info) >= price:
            context['result'] = result
            return render(request, 'index.html', context)

    return render(request, 'index.html')
