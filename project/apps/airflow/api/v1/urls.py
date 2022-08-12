from django.urls import path

from .views import search, get_exchange_rate_manually

urlpatterns = [
    path("search/", search, name='airflow-search'),
    path("exchange_rate/", get_exchange_rate_manually, name='exchange_rate'),
]
