from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger uchun konfiguratsiya
schema_view = get_schema_view(
    openapi.Info(
        title="Video API",
        default_version='v1',
        description="Video yuklash va ko'rish uchun API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('main.urls')),  # main.urls orqali barcha API URL'larini import qilish
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI uchun
]
