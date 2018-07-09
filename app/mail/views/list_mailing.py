from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from mail.models import Receiver, SelectedTicket
from ticket.models.ticketdata import TicketData
from django.core.exceptions import ObjectDoesNotExist

# from store.exceptions import OutOfStock

__all__ = (
    'list_mailing',
)


def list_mailing(request):
    from_mail_address = 'devhsj@gmail.com'
    title = 'TicketList'

    context = {}

    if request.method == "POST":
        to_mail_address = request.POST['mail_address']
        price_lists = []
        if to_mail_address:
            receiver_list = Receiver.objects.filter(mail_address=to_mail_address)
            for receiver in receiver_list:

                ticket_query_set = TicketData.objects.filter(
                    destination_place=receiver.destination_place,
                    origin_place=receiver.origin_place,
                    ticket_price__lte=receiver.user_max_price,
                    departure_date=receiver.departure_date
                )
                for ticket in ticket_query_set:
                    s,created = SelectedTicket.objects.get_or_create(receiver=receiver, ticket_data=ticket)
                    price_lists.append({
                        'mail_address': s.receiver.mail_address,
                        'user_max_price': s.receiver.user_max_price,
                        'origin_place': s.receiver.origin_place,
                        'destination_place': s.receiver.destination_place,
                        'departure_date': s.ticket_data.departure_date,
                        'departure_datetime': s.ticket_data.departure_datetime,
                        'ticket_price': s.ticket_data.ticket_price
                    })

                context = {
                    'price_lists': price_lists,

                }
        else:
            selected_ticket_list = SelectedTicket.objects.all()
            for selected_ticket in selected_ticket_list:
                price_lists.append({
                    'mail_address': selected_ticket.receiver.mail_address,
                    'user_max_price': selected_ticket.receiver.user_max_price,
                    'origin_place': selected_ticket.receiver.origin_place,
                    'destination_place': selected_ticket.receiver.destination_place,
                    'departure_date': selected_ticket.ticket_data.departure_date,
                    'departure_datetime': selected_ticket.ticket_data.departure_datetime,
                    'ticket_price': selected_ticket.ticket_data.ticket_price
                })
            return render(request, 'ticket/list.html', context={'price_lists': price_lists})

        # except Receiver.DoesNotExist as e:
        #     return redirect('mail:mail-list')

        if 'send_mail' in request.POST:
            contents = render_to_string('mail_form.html', context)

            msg = EmailMessage(title, contents, to=[to_mail_address], from_email=from_mail_address)
            msg.content_subtype = "html"
            msg.send()
    return render(request, 'ticket/list.html', context)
