from django.db import models


class City_Infomation(models.Model):
    CITY_CODE_SEOUL = '서울'
    CITY_CODE_PUSAN = '부산'
    CITY_CODE_INCHEON = '인천'
    CITY_CODE_GIMPO = '김포'
    CITY_CODE_ROMA = '로마'
    CITY_CODE_FLORENCE = '피렌체'

    CHOICES_CITY_TYPE = (
        (CITY_CODE_SEOUL, 'SEL'),
        (CITY_CODE_PUSAN, 'PUS'),
        (CITY_CODE_INCHEON, 'ICN'),
        (CITY_CODE_GIMPO, 'GMP'),
        (CITY_CODE_ROMA, 'ROM'),
        (CITY_CODE_FLORENCE, 'FLR'),
    )
    cityname = models.CharField('도시명', max_length=3, choices=CHOICES_CITY_TYPE, blank=True)


# Create your models here.
class TicketInfomation(models.Model):
    startcity = models.ForeignKey(City_Infomation, verbose_name='출발도시',related_name='start', blank=True, on_delete=models.CASCADE)
    arrivecity = models.ForeignKey(City_Infomation, verbose_name='도착도시',related_name='arrive', blank=True, on_delete=models.CASCADE)
    startdate = models.DateField('출발날짜', )
    enddate = models.DateField('도착날짜', )
    price = models.CharField('가격', max_length=200, )
