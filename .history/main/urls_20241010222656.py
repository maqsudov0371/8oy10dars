from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]



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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)),  # VideoViewSet uchun URL
]
