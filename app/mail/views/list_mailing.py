from django.core.mail import EmailMessage
from django.shortcuts import render
from django.template.loader import render_to_string

from mail.models import Receiver
from ticket.models.ticketdata import TicketData

__all__ = (
    'list_mailing',
)


def list_mailing(request):
    from_mail_address = 'devhsj@gmail.com'
    title = 'TicketList'

    context = {}

    if request.method == "POST":
        to_mail_address = request.POST['mail_address']
        receiver_lists = Receiver.objects.filter(mail_address=to_mail_address)

        price_lists = []
        for receiver_list in receiver_lists:
            ticket_query_set = TicketData.objects.filter(
                origin_place=receiver_list.origin_place,
                destination_place=receiver_list.destination_place,
                ticket_price__lte=receiver_list.user_max_price,
                departure_date=receiver_list.departure_date
            )

            for ticket in ticket_query_set:
                price_lists.append({
                    'mail_address': receiver_list.mail_address,
                    'user_max_price': receiver_list.user_max_price,
                    'departure_date': ticket.departure_date,
                    'departure_datetime': ticket.departure_datetime,
                    'ticket_price': ticket.ticket_price
                })
        context = {
            'price_lists': price_lists
        }
        if 'send_mail' in request.POST:
            contents = render_to_string('mail_form.html', context)

            msg = EmailMessage(title, contents, to=[to_mail_address], from_email=from_mail_address)
            msg.content_subtype = "html"
            msg.send()
    return render(request, 'ticket/list.html', context)
