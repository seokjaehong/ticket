from django.urls import path
from mail import views

app_name = 'mail'
urlpatterns = [
    path('add/', views.add_mailing, name='mail-add'),
    path('list/', views.list_mailing, name='mail-list'),
]
