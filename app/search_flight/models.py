from django.db import models


# Create your models here.
class TicketInfomation(models.Model):
    startcity = models.CharField('출발도시', max_length=200, blank=True)
    arrivecity = models.CharField('도착도시', max_length=200, blank=True)
    startdate = models.DateField('출발날짜', )
    enddate = models.DateField('도착날짜', )
    price = models.CharField('가격',max_length=200,)
