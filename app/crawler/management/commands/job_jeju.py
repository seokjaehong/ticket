from django.core.management import BaseCommand

from ticket.tasks import get_ticket_information_save_7C, get_ticket_information_save_BX, get_ticket_information_save_KE, \
    get_ticket_information_save_LJ, get_ticket_information_save_OZ, get_ticket_information_save_TW, \
    get_ticket_information_save_ZE


class Command(BaseCommand):
    def handle(self, *args, **options):
        from ticket.models.ticketdata import TicketData

        TicketData.objects.all().delete()

        get_ticket_information_save_TW.delay()
        get_ticket_information_save_7C.delay()
        get_ticket_information_save_BX.delay()
        get_ticket_information_save_KE.delay()
        get_ticket_information_save_LJ.delay()
        get_ticket_information_save_OZ.delay()
        get_ticket_information_save_ZE.delay()
