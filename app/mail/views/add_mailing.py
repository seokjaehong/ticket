from django.shortcuts import render, redirect

from mail.forms import MailingListForm
from mail.models import Receiver, SelectedTicket
from ticket.models.ticketdata import TicketData

__all__ = (
    'add_mailing',
)


def add_mailing(request):
    """
     Template: ticket/add.html
        form (email, departure_date, price를 받아서 저장)
    1. form에 주어진 조건으로 database에서 max_price보다 적은 가격의 검색 결과를 보여줌
    2. 추가하고나면, 리스
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = MailingListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            receiver_list = Receiver.objects.filter(mail_address=request.POST['mail_address'])
            for receiver in receiver_list:
                ticket_list = TicketData.objects.filter(
                    destination_place=receiver.destination_place,
                    origin_place=receiver.origin_place,
                    ticket_price__lte=receiver.user_max_price,
                    departure_date=receiver.departure_date
                )
                for ticket in ticket_list:
                    selected_ticket, created = SelectedTicket.objects.get_or_create(
                        receiver=receiver,
                        ticket_data=ticket
                    )
                    selected_ticket.save()
            return redirect('mail:mail-list')
    else:
        form = MailingListForm()
        context = {
            'form': form,

        }
        return render(request, 'ticket/add.html', context)
