from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from mail.models import Receiver, SelectedTicket
from ticket.models.ticketdata import TicketData

__all__ = (
    'list_mailing',
)


def list_mailing(request):
    from_mail_address = 'devhsj@gmail.com'
    title = 'TicketList'
    price_lists = []
    context = {}

    if request.method == "POST":
        to_mail_address = request.POST['mail_address']

        if to_mail_address:
            receiver_list = Receiver.objects.filter(mail_address=to_mail_address)
        else:
            receiver_list = Receiver.objects.all()

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
                    ticket_data=ticket,
                )
                selected_ticket.save()

                price_lists.append({
                    'mail_address': selected_ticket.receiver.mail_address,
                    'user_max_price': selected_ticket.receiver.user_max_price,
                    'origin_place': selected_ticket.receiver.origin_place,
                    'destination_place': selected_ticket.receiver.destination_place,
                    'departure_date': selected_ticket.ticket_data.departure_date,
                    'departure_datetime': selected_ticket.ticket_data.departure_datetime,
                    'ticket_price': selected_ticket.ticket_data.ticket_price
                })

        if 'send_mail' in request.POST:
            contents = render_to_string('mail_form.html', {'price_lists': price_lists})

            msg = EmailMessage(title, contents, to=[to_mail_address], from_email=from_mail_address)
            msg.content_subtype = "html"
            msg.send()
    return render(request, 'ticket/list.html', {'price_lists':price_lists})
