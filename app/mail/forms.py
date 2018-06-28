from django.forms import ModelForm
from django import forms

from .models import Receiver

__all__ = (
    'MailingListForm',
)


class MailingListForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ['mail_address','username','departure_date','user_max_price','origin_place','destination_place'
                  ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
