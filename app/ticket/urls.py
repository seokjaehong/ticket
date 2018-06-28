from django.urls import include, path

from ticket import views

app_name='ticket'

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.ticket_search, name='ticket-search'),
    path('search/tway/', views.ticket_search_from_tway, name='ticket-search-from-tway'),
]
