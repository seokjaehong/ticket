from django.urls import path
from mail import views

app_name = 'mail'
urlpatterns = [
    path('add_mailing/', views.add_mailing, name='add-mailing'),
    path('send_mail/', views.send_mail, name='send-mail'),
    path('list_mailing/', views.list_mailing, name='list-mailing'),
]
