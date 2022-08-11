from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from .swagger import swagger_patterns

api_v1_patterns = [
    path('provider_a/', include('provider_a.api.v1.urls'))
]

api_patterns = [
    path('v1/', include(api_v1_patterns)),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    api_v1_patterns += swagger_patterns
    urlpatterns += (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
    urlpatterns += staticfiles_urlpatterns()
