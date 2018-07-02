from django.urls import path
from mail import views

app_name = 'mail'
urlpatterns = [
    path('add_mailing/', views.add_mailing, name='mail-add'),
    path('list_mailing/', views.list_mailing, name='mail-list'),
]
