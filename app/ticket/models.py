from django.db import models

__all__ = (
    'TicketData',
)


# Create your models here.
class TicketData(models.Model):
    goreturn = models.CharField('출발/도착 구분', max_length=2)

    departure_date = models.DateField('출발날짜', blank=True)
    departure_duration = models.CharField('소요시간', max_length=100)
    country = models.CharField('출발나라', max_length=50)
    departure_city = models.CharField('출발도시', max_length=50)
    arrival_city = models.CharField('도착도시', max_length=50)
    flight_company = models.CharField('항공사명', max_length=20)

    ticket_price = models.IntegerField('가격')

    currency = models.CharField('환율', max_length=10, blank=True)
    fee_policy = models.CharField('요금규정', max_length=100, blank=True)

    data_source = models.CharField('데이터 출처', max_length=30)
    # url_link = models.URLField('데이터 링크',blac)

    is_delete = models.BooleanField('삭제데이터여부', default=False)
    create_datetime = models.DateTimeField('생성시간', auto_now_add=True)
    modify_datetime = models.DateTimeField('수정시간', auto_now_add=True)
    description = models.CharField('설명', max_length=200, blank=True, null=True)
