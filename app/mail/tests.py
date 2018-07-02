import datetime

from django.test import TestCase

# Create your tests here.

from .models import Receiver
from ticket.models.ticketdata import TicketData


class ReceiverModelTest(TestCase):
    MODEL_RECEIVER = Receiver
    CREATE_NUM = 10
    TEST_MAIL_ADDRESS = 'devhsj@gmail.com'
    TEST_USERNAME = 'Hong'
    TEST_ORIGIN_PLACE = 'GMP'
    TEST_DESTINATION_PLACE = 'CJU'

    def create_receiver(self):
        r1 = self.MODEL_RECEIVER.object.create(
            id=1,
            mail_address=self.TEST_MAIL_ADDRESS,
            username=self.TEST_USERNAME,
            departure_date=datetime.date.today(),
            origin_place=self.TEST_ORIGIN_PLACE,
            destination_place=self.TEST_DESTINATION_PLACE,
            user_max_price=50000,
        )
        r1.save()
        t1 = TicketData.objects.create(
            origin_place=self.TEST_ORIGIN_PLACE,
            destination_place=self.TEST_DESTINATION_PLACE,
            is_direct=False,
            way_point='',
            way_point_duration='',
            ticket_price=40000,
            departure_date=datetime.date.today(),
            departure_datetime='12:00',
            arrival_date=datetime.date.today(),
            arrival_datetime='1:00',
            flight_time='01:15',
            leftseat='2',
            flight_company='TWAY',
            currency='KRW',
            data_source='TWAY'
        )
        t1.save()
        r1.ticket.create(t1)

        self.assertEqual(r1.mail_address,self.TEST_MAIL_ADDRESS)
        self.assertEqual(r1.username,self.TEST_USERNAME)
