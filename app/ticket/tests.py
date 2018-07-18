from datetime import date, timedelta

from django.test import TestCase

from crawler.utils import daterange,  get_ticket_information_single_date
from mail.models import SelectedTicket, Receiver
from ticket.models.ticketdata import TicketData

# Create your tests here.
# test case 1 ) data가 없을 때: data crawling -> mail add -> SelectedTicket data check
# test case 2 ) data가 있을 때: mail add -> SelectedTicket data check
# test case 3 ) data도 있고 mail도 있고, mail 추가 or data추
# date.today()로 하면 저녁에 했을 때 티켓이 없으므로 하루날짜뒤로 테스트

class TestCrawling(TestCase):
    MODEL_TICKET_DATA = TicketData
    MODEL_SELECTED_TICKET = SelectedTicket
    MODEL_RECEIVER = Receiver
    CREATE_NUM = 1
    TEST_DEPARTURE_DATE = date.today() + timedelta(days=1)
    TEST_EDATE = TEST_DEPARTURE_DATE + timedelta(days=CREATE_NUM)
    TEST_ORIGIN_PLACE = '김포'
    TEST_ORIGIN_PLACE_CODE = 'GMP'
    TEST_DESTINATION_PLACE = '제주'
    TEST_DESTINATION_PLACE_CODE = 'CJU'
    TEST_FLIGHT_COMPANY = 'OZ'
    TEST_MAIL_ADDRESS = 'devhsj@gmail.com'
    TEST_USERNAME = 'Hong'
    TEST_USER_MAX_PRICE = 50000

    def test_create_ticket_data(self):
        TicketData.objects.all().delete()

        for single_date in daterange(self.TEST_DEPARTURE_DATE, self.TEST_EDATE):
            r = get_ticket_information_single_date(self.TEST_ORIGIN_PLACE_CODE, self.TEST_DESTINATION_PLACE_CODE,
                                                   str(single_date), self.TEST_FLIGHT_COMPANY)
        self.assertEqual()

    def test_create_receiver(self):
        r1 = self.MODEL_RECEIVER.objects.create(
            id=1,
            mail_address=self.TEST_MAIL_ADDRESS,
            username=self.TEST_USERNAME,
            departure_date=self.TEST_DEPARTURE_DATE,
            origin_place=self.TEST_ORIGIN_PLACE,
            destination_place=self.TEST_DESTINATION_PLACE,
            user_max_price=self.TEST_USER_MAX_PRICE,
        )
        self.assertEqual(r1.mail_address, self.TEST_MAIL_ADDRESS)
        self.assertEqual(r1.username, self.TEST_USERNAME)
        self.assertEqual(r1.departure_date, self.TEST_DEPARTURE_DATE)
        self.assertEqual(r1.origin_place, self.TEST_ORIGIN_PLACE)
        self.assertEqual(r1.destination_place, self.TEST_DESTINATION_PLACE)
        self.assertEqual(r1.user_max_price, self.TEST_USER_MAX_PRICE)

    def test_create_selected_ticket(self):
        receiver_list = Receiver.objects.all()
        for receiver in receiver_list:
            ticket_list = TicketData.objects.filter(
                destination_place=receiver.destination_place,
                origin_place=receiver.origin_place,
                ticket_price__lte=receiver.user_max_price,
                departure_date=receiver.departure_date
            )
            for ticket in ticket_list:
                selected_ticket, created = SelectedTicket.objects.get_or_create(
                    receiver=receiver,
                    ticket_data=ticket
                )
                selected_ticket.save()

                self.assertEqual(SelectedTicket.objects.all().count(), selected_ticket.count())
