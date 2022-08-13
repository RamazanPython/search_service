from django.urls import path

from .views import search, get_exchange_rate_manually, results

urlpatterns = [
    path("search/", search, name='airflow-search'),
    path("exchange_rate/", get_exchange_rate_manually, name='exchange_rate'),
    path("results/<uuid:search_id>/<str:currency>/", results, name='results')
]
