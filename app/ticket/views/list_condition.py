from django.shortcuts import render

from ..models.mail_condition import MailCondition

__all__=(
    'list_condition',
)

def list_condition(request):
    mail_lists = MailCondition.objects.all()
    context = {
        'mail_lists': mail_lists,
    }
    return render(
        request, 'ticket/list.html', context
    )
