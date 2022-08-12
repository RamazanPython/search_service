from django.urls import path

from .views import search, exchange_rate

urlpatterns = [
    path("search/", search, name='airflow-search'),
    path("exchange_rate/", exchange_rate, name='exchange_rate'),
]
