from django.core.management import BaseCommand
from django.utils import timezone

from crawler.twayair import TwayData
from datetime import timedelta, date
import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        from ticket.models.ticketdata import TicketData
        from mail.models import Receiver
        pass
