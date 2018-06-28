from django.shortcuts import render

from mail.models import Receiver

__all__=(
    'list_mailing',
)

def list_mailing(request):
    mail_lists = Receiver.objects.all()
    context = {
        'mail_lists': mail_lists,
    }
    return render(request, 'ticket/list.html', context)
