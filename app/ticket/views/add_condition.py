from django.shortcuts import render, redirect

from ticket.forms import MailingListForm

__all__ = (
    'add_condition',
)


def add_condition(request):
    """
     Template: ticket/add.html
        form (email, departure_date, price를 받아서 저장)
    1. form에 주어진 조건으로 database에서 max_price보다 적은 가격의 검색 결과를 보여줌
    2.
    :param request:
    :return:
    """
    email = request.GET.get('email')
    departure_date = request.GET.get('departure_date')
    user_max_price = request.GET.get('user_max_price')
    username = request.GET.get('username')

    print(email)
    print(request.method)

    if request.method=='POST':
        form = MailingListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ticket:list-condition')
    else:
        form = MailingListForm()
    context = {
        'form':form,

    }
    return render(request,'ticket/add.html',context)
