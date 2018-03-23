from django.shortcuts import render


# Create your views here.

def SearchFlight(request):

    context = dict()

    if request.method == 'POST':
        startcity = request.POST['startcity']
        arrivecity = request.POST['arrivecity']
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        price = request.POST['price']





    return render(request, 'index.html')
