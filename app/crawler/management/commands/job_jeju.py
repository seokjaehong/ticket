import time

from django.core.management import BaseCommand

from crawler.utils import daterange
from ticket.tasks import get_ticket_information_save_7C, get_ticket_information_save_BX, \
    get_ticket_information_save_KE, get_ticket_information_save_LJ, get_ticket_information_save_OZ, \
    get_ticket_information_save_TW, \
    get_ticket_information_save_ZE

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
            get_ticket_information_save_TW.delay(single_date)
            get_ticket_information_save_7C.delay(single_date)
            get_ticket_information_save_BX.delay(single_date)
            get_ticket_information_save_KE.delay(single_date)
            get_ticket_information_save_LJ.delay(single_date)
            get_ticket_information_save_OZ.delay(single_date)
            get_ticket_information_save_ZE.delay(single_date)

        print("---(maximize) %s seconds ---" % (time.time() - start_time))
