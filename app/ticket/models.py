from django.db import models


# Create your models here.
class TicketData(models):
    departure_month = models.CharField('출발 월', max_length=2, blank=True)
    arrival_month = models.CharField('도착 월', max_length=2, blank=True)

    departure_datetime = models.DateTimeField('출발날짜', blank=True)
    arrival_datetime = models.DateTimeField('도착날짜', blank=True)

    departure_country = models.CharField('출발나라', max_length=50)
    departure_city = models.CharField('출발도시', max_length=50)
    arrival_country = models.CharField('도착나라', max_length=50)
    arrival_city = models.CharField('도착도시', max_length=50)

    flight_company = models.CharField('항공사명', max_length=20)
    flight_number = models.CharField('항공편명', max_length=20)
    validity = models.CharField('유효기간', max_length=10, blank=True)

    ticket_price = models.IntegerField('가격')
    currency = models.CharField('환율', max_length=10)
    fee_policy = models.CharField('요금규정', max_length=100)

    data_source = models.CharField('데이터 출처', max_length=30)
    data_link = models.URLField('데이터 링크')
    data_message = models.CharField('데이터 메세지', max_length=200, blank=True)

    is_delete = models.BooleanField('삭제데이터여부', default=False)
    create_datetime = models.DateTimeField('생성시간', auto_now_add=True)
    modify_datetime = models.DateTimeField('수정시간', auto_now_add=True)
    description = models.CharField('설명', max_length=200)


class oneway(TicketData):
    pass

class returnway(TicketData):
    pass