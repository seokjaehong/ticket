from django.db import models

__all__ = (
    'MailCondition',
)


# Create your models here.
class MailCondition(models.Model):
    mail_address = models.CharField('email address', max_length=40)
    username = models.CharField('사용자 이름', max_length=30, blank=True, null=True)
    departure_date = models.DateField('출발날짜')
    user_max_price = models.IntegerField('최대가격')



