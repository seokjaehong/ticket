from django.urls import include, path

from ticket import views

urlpatterns = [
    path('search/', views.ticket_search, name='ticket_search'),
    # path('list/,')
    # path('search/list', views.ticket_search_from_database, name='ticket_search_from_database')
]
