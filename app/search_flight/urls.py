from django.urls import path

from .views import SearchFlight

urlpatterns = [
    path('search/', SearchFlight, name='search-flight')
]
