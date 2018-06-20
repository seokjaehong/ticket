from django.db import models

from ..models.mail_condition import MailCondition
from ..models.ticketdata import TicketData



class MailHistory(models.Model):
    mail_address = models.ForeignKey(MailCondition, on_delete=models.CASCADE)
    ticket_data = models.ForeignKey(TicketData, on_delete=models.CASCADE)
    create_datetime = models.DateTimeField('생성시간',auto_now_add=True)