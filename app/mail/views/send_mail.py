from django.core.mail import EmailMessage
from django.shortcuts import render

from django.core.mail import send_mail

__all__ = (
    'send_mail',
)


def send_mail(request):
    # 1. send_mail
    if request.method == "POST":
        to_mail_address = [request.POST['mail_address']]
        title = request.POST['title']
        contents = request.POST['contents']
        from_mail_address = 'devhsj@gmail.com'
        send_mail(title, contents, from_mail_address, to_mail_address)

    return render(request, 'ticket/send_mail.html')
