from django.shortcuts import render, redirect

from mail.forms import MailingListForm

__all__ = (
    'add_mailing',
)


def add_mailing(request):
    """
     Template: ticket/add.html
        form (email, departure_date, price를 받아서 저장)
    1. form에 주어진 조건으로 database에서 max_price보다 적은 가격의 검색 결과를 보여줌
    2.
    :param request:
    :return:
    """
    if request.method=='POST':
        form = MailingListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mail:list-mailing')
    else:
        form = MailingListForm()

    context = {
        'form':form,

    }
    return render(request,'ticket/add.html',context)
