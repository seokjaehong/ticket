from django.db import models


# Create your models here.
class TicketInfomation(models.Model):
    startcity = models.CharField('출발도시', max_length=200, blank=True)
    arrivecity = models.CharField('도착도시', max_length=200, blank=True)
    startdate = models.DateField('출발날짜', )
    enddate = models.DateField('도착날짜', )
    price = models.CharField('가격', max_length=200, )


class City_Infomation(models.Model):
    CITY_CODE_SEOUL = 'SEL'
    CITY_CODE_PUSAN = 'PUS'
    CITY_CODE_INCHEON = 'ICN'
    CITY_CODE_GIMPO = 'GMP'
    CITY_CODE_ROMA = 'ROM'
    CITY_CODE_FLORENCE = 'FLR'
    CHOICES_BLOOD_TYPE = (
        (CITY_CODE_SEOUL, '서울'),
        (CITY_CODE_PUSAN, '부산'),
        (CITY_CODE_INCHEON, '인천'),
        (CITY_CODE_GIMPO, '김포'),
        (CITY_CODE_ROMA, '로마'),
        (CITY_CODE_FLORENCE, '피렌체'),
    )
    cityname = models.CharField('도시명', max_length=3, choices=CHOICES_BLOOD_TYPE, blank=True)
