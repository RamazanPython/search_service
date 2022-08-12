from django.urls import path

from utils.consts import ProvidersUrlNameChoice

from .views import search

urlpatterns = [
    path("search/", search, name=ProvidersUrlNameChoice.PROVIDER_A.value),
]
