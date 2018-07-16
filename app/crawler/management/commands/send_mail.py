from django.core.mail import EmailMessage
from django.core.management import BaseCommand
from django.template.loader import render_to_string

from mail.models import Receiver, SelectedTicket


class Command(BaseCommand):
    def handle(self, *args, **options):

        receiver_list = SelectedTicket.objects.all().distinct('receiver')
        for receiver in receiver_list:

            mail_lists = SelectedTicket.objects.filter(receiver__mail_address=receiver.receiver.mail_address)
            price_lists = []
            for mail_list in mail_lists:
                price_lists.append({
                    'flight_company':mail_list.ticket_data.flight_company,
                    'user_max_price': mail_list.receiver.user_max_price,
                    'origin_place': mail_list.receiver.origin_place,
                    'destination_place': mail_list.receiver.destination_place,
                    'departure_date': mail_list.receiver.departure_date,
                    'departure_datetime': mail_list.ticket_data.departure_datetime,
                    'ticket_price': mail_list.ticket_data.ticket_price
                })
            context = {
                'price_lists': price_lists
            }

            contents = render_to_string('mail_form.html', context)
            msg = EmailMessage(subject='Ticket-List',
                               body=contents,
                               to=[receiver.receiver.mail_address],
                               from_email='hsj2334@gmail.com')
            msg.content_subtype = "html"
            msg.send()

