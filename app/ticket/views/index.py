from django.shortcuts import render

from ..models.ticketdata import TicketData


def index(request):
    tickets = TicketData.objects.all()
    context = {
        'tickets': tickets
    }
    return render(request, 'base.html', context)
