from django.urls import include, path

from .views import provider_a

urlpatterns = [
    path(r'search/', provider_a.ProviderAViewSet, name='provider-a-search')
]
