from django.urls import path

from .views import SearchFlight, add_flight

urlpatterns = [
    path('search/', SearchFlight, name='search-flight'),
    path('add/', add_flight, name='add-flight')
]
