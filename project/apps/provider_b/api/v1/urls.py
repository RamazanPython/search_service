from django.urls import path

from utils.consts import ProvidersUrlNameChoice

from .views import provider_b

urlpatterns = [
    path("search/", provider_b.search, name=ProvidersUrlNameChoice.PROVIDER_B.value),
]
