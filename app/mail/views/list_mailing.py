from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from mail.models import Receiver
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
            receiver_list = Receiver.objects.filter(mail_address=to_mail_address).prefetch_related('ticket')
            for receiver in receiver_list:

                ticket_query_set = TicketData.objects.filter(
                    destination_place=receiver.destination_place,
                    origin_place=receiver.origin_place,
                    ticket_price__lte=receiver.user_max_price,
                    departure_date=receiver.departure_date
                )
                for ticket in ticket_query_set:
                    receiver.ticket.add(ticket)
                    price_lists.append({
                        'mail_address': receiver.mail_address,
                        'user_max_price': receiver.user_max_price,
                        'origin_place': receiver.origin_place,
                        'destination_place':receiver.destination_place,
                        'departure_date': ticket.departure_date,
                        'departure_datetime': ticket.departure_datetime,
                        'ticket_price': ticket.ticket_price
                    })

                context = {
                    'price_lists': price_lists
                }
        else:
            receiver_list=Receiver.objects.all()
            # for receiver in receiver_list:
            #     price_lists.append({
            #         'mail_address': receiver.mail_address,
            #         'user_max_price': receiver.user_max_price,
            #         'origin_place': receiver.origin_place,
            #         'destination_place': receiver.destination_place,
            #         'departure_date': receiver.tickets.departure_date,
            #         'departure_datetime': receiver.tickets.departure_datetime,
            #         'ticket_price': receiver.tickets.ticket_price
            #     })
            return render(request,'ticket/list.html',context={'price_lists':receiver_list})


        # except Receiver.DoesNotExist as e:
        #     return redirect('mail:mail-list')

        if 'send_mail' in request.POST:
            contents = render_to_string('mail_form.html', context)

            msg = EmailMessage(title, contents, to=[to_mail_address], from_email=from_mail_address)
            msg.content_subtype = "html"
            msg.send()
    return render(request, 'ticket/list.html', context)
