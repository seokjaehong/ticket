from django.core.mail import EmailMessage
from django.shortcuts import render
from django.core.mail import send_mail

from ticket.models.ticketdata import TicketData
from ..models import Receiver

from django.template.loader import render_to_string

__all__ = (
    'send_mail',
)


def send_mail(request):
    if request.method =='POST':
        receiver_lists = Receiver.objects.all()

        for receiver_list in receiver_lists:

            ticket_query_set = TicketData.objects.filter(
                origin_place=receiver_list.origin_place,
                destination_place=receiver_list.destination_place,
                ticket_price__lte=receiver_list.user_max_price,
                departure_date=receiver_list.departure_date
            )
            for ticket in ticket_query_set:
                receiver_list.ticket.add(ticket)

            contents_price_list = receiver_list.objects.all().values('departure_datetime','ticket_price')

        to_mail_address = [request.POST['mail_address']]
        from_mail_address = 'devhsj@gmail.com'
        title = 'Ticket List'
        contents = render_to_string('mail_form', contents_price_list)

        EmailMessage(title,contents,to=to_mail_address,from_email=from_mail_address).send()
    # send_mail(title, contents, from_mail_address, to_mail_address)

    return render(request, 'ticket/add.html')
