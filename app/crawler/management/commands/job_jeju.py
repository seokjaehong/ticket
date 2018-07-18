import time

from django.core.management import BaseCommand

from crawler.utils import daterange, create_select_mail_list
from ticket.tasks import get_ticket_information_save

import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        from ticket.models.ticketdata import TicketData
        start_time = time.time()
        TicketData.objects.all().delete()
        add_days = 10
        departure_date = datetime.date.today()
        edate = departure_date + datetime.timedelta(days=add_days)

        for single_date in daterange(departure_date, edate):
            get_ticket_information_save.delay(single_date, 'TW')
            get_ticket_information_save.delay(single_date, 'LJ')
            get_ticket_information_save.delay(single_date, 'KE')
            get_ticket_information_save.delay(single_date, 'OZ')
            get_ticket_information_save.delay(single_date, 'BX')
            get_ticket_information_save.delay(single_date, '7C')
            get_ticket_information_save.delay(single_date, 'ZE')

        print("---(celery_excute) %s seconds ---" % (time.time() - start_time))

