from django.urls import include, path

from .views import search

urlpatterns = [
    path("search/", search, name='provider-a-search'),
]
