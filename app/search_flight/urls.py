from django.urls import path

from mail.views import send_email
from .views import SearchFlight

urlpatterns = [
    path('search/', SearchFlight, name='search-flight'),

]
