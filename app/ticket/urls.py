from django.urls import include, path

from ticket import views

app_name = 'ticket'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.ticket_search, name='ticket-search'),
    path('search/jeju/', views.ticket_search_from_jeju, name='ticket-search-from-jeju'),
]
