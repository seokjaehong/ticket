from django.forms import ModelForm
from django import forms

from .models.mail_condition import MailCondition

__all__ = (
    'MailingListForm',
)


class MailingListForm(forms.ModelForm):
    class Meta:
        model = MailCondition
        fields = ['mail_address','username','departure_date','user_max_price'
                  ]
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
