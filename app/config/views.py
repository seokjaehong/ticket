from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

from ticket.models import TicketData


def index(request):
    tickets = TicketData.objects.all()
    context = {
        'tickets': tickets
    }
    print(context)
    # return HttpResponse('Hello')
    # return render(request,'base.html',context)
    return render(request, 'base.html', context)
#