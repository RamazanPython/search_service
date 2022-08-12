from django.urls import path

from .views import provider_b

urlpatterns = [
    path("search/", provider_b.search, name='provider-b-search'),
]
