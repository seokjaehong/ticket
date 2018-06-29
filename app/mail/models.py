from django.db import models

# Create your models here.
from django.db import models

from ticket.models.ticketdata import TicketData

__all__ = (
    'Receiver',
)


# Create your models here.
class Receiver(models.Model):
    mail_address = models.CharField('email address', max_length=40)
    username = models.CharField('사용자 이름', max_length=30, blank=True, null=True)
    departure_date = models.DateField('출발날짜')
    origin_place = models.CharField('출발도시', max_length=50)
    destination_place = models.CharField('도착도시', max_length=50)
    user_max_price = models.IntegerField('최대가격')
    ticket = models.ManyToManyField(TicketData)

    class Meta:
        ordering =('departure_date',)



