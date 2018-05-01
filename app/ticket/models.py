from django.db import models


# Create your models here.
class TicketData(models):
    departure_datetime = models.DateTimeField('출발날짜')
    arrival_datetime = models.DateTimeField('도착날짜')
    ticket_price = models.IntegerField('가격')
    currency = models.CharField('환율', max_length=10)
    departure_city = models.CharField('출발도시', max_length=50)
    arrival_city = models.CharField('도착도시', max_length=50)
