from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view( #информация и права доступа к ui swagger документации api
    openapi.Info(
        title="Contact Book API",
        default_version='v1',
        description="API for managing contacts",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('contact_api.urls')), # пути эндпоинтов api
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)), #openapi документация
]
