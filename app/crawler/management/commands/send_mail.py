from django.core.management import BaseCommand
from django.utils import timezone

from crawler.twayair import TwayData
from datetime import timedelta, date
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        from ticket.models.ticketdata import TicketData
        from ticket.models.mail_condition import MailCondition

        mailing_list = MailCondition.objects.all()




        # for single_ticket_data in ticket_data_list:
        #     for ticket_data in single_ticket_data:
        #         ticket, _ = TicketData.objects.update_or_create(
        #             origin_place=ticket_data['origin_place'],
        #             destination_place=ticket_data['destination_place'],
        #             is_direct=ticket_data['is_direct'],
        #             way_point=ticket_data['way_point'],
        #             way_point_duration=ticket_data['way_point_duration'],
        #             ticket_price=ticket_data['ticket_price'],
        #
        #             departure_date=ticket_data['departure_date'],
        #             departure_datetime=ticket_data['departure_datetime'],
        #             arrival_date=ticket_data['arrival_date'],
        #             arrival_datetime=ticket_data['arrival_datetime'],
        #             flight_time=ticket_data['flight_time'],
        #             flight_company=ticket_data['flight_company'],
        #             currency=ticket_data['currency'],
        #             data_source=ticket_data['data_source'],
        #             leftseat=ticket_data['leftseat'],
        #
        #             # modify_datetime=datetime.datetime.now(tz=timezone.utc)
        #         )
