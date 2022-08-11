import os
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

swagger_patterns = [
    path('swagger/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('swagger/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
