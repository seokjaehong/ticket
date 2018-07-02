from django.core.mail import EmailMessage
from django.core.management import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone

from crawler.twayair import TwayData
from datetime import timedelta, date
import datetime

from ticket.models.ticketdata import TicketData
from mail.models import Receiver


class Command(BaseCommand):
    def handle(self, *args, **options):
        receiver_list = Receiver.objects.all()

        for receiver in receiver_list:
            ticket_query_set = TicketData.objects.filter(
                destination_place=receiver.destination_place,
                origin_place=receiver.origin_place,
                ticket_price__lte=receiver.user_max_price,
                departure_date=receiver.departure_date
            )
            price_lists = []
            for ticket in ticket_query_set:
                receiver.ticket.add(ticket)
                price_lists.append({
                    'mail_address': receiver.mail_address,
                    'user_max_price': receiver.user_max_price,
                    'origin_place': receiver.origin_place,
                    'destination_place': receiver.destination_place,
                    'departure_date': ticket.departure_date,
                    'departure_datetime': ticket.departure_datetime,
                    'ticket_price': ticket.ticket_price
                })

            context = {
                'price_lists': price_lists
            }

            contents = render_to_string('mail_form.html', context)

            msg = EmailMessage(subject='Ticket-List',
                               body=contents,
                               to=[receiver.mail_address],
                               from_email='hsj2334@gmail.com')
            msg.content_subtype = "html"
            msg.send()
