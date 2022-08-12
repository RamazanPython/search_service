from django.urls import path

from .views import search

urlpatterns = [
    path("search/", search, name='provider-a-search'),
]
