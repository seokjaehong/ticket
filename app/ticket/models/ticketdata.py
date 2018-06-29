from django.db import models
from django.shortcuts import get_object_or_404

__all__ = (
    'TicketData',
)


# Create your models here.
class TicketData(models.Model):
    # ticketID = models.IntegerField('티켓ID', unique=True)
    origin_place = models.CharField('출발도시', max_length=50)
    destination_place = models.CharField('도착도시', max_length=50)
    is_direct = models.BooleanField('경유여부', default=False)
    way_point = models.CharField('경유지', max_length=50)
    way_point_duration = models.CharField('경유시간', max_length=10)
    ticket_price = models.IntegerField('가격')

    departure_date = models.DateField('출발날짜')
    departure_datetime = models.CharField('출발시간', max_length=10)

    arrival_date = models.DateField('도착날짜')
    arrival_datetime = models.CharField('도착시간', max_length=10)
    flight_time = models.CharField('총소요시간', max_length=100)

    leftseat = models.CharField('잔여좌석', max_length=30, blank=True)

    flight_company = models.CharField('항공사명', max_length=20)
    currency = models.CharField('환율', max_length=10, blank=True)
    data_source = models.CharField('데이터 출처', max_length=30)

    is_delete = models.BooleanField('삭제데이터여부', default=False)
    create_datetime = models.DateTimeField('생성시간', auto_now_add=True)
    modify_datetime = models.DateTimeField('수정시간', auto_now_add=True)
    description = models.CharField('설명', max_length=200, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return '(%s) %s, %s : %s' % (self.pk,self.departure_date, self.departure_datetime, self.ticket_price)

    class Meta:
        ordering =('departure_date','departure_datetime',)