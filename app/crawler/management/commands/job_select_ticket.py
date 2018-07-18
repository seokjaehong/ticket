from django.core.management import BaseCommand

from crawler.utils import create_select_mail_list


class Command(BaseCommand):
    def handle(self, *args, **options):
        create_select_mail_list()