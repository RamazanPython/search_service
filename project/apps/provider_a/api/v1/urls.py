from django.urls import include, path

from .views import provider_a

urlpatterns = [
    path("search/", provider_a.search, name='provider-a-search'),
]
