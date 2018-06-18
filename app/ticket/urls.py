from django.urls import include, path

from ticket import views

urlpatterns = [
    path('search/', views.ticket_search, name='ticket_search'),
    path('search/tway', views.ticket_search_from_tway,name='ticket_search_from_tway'),
]
