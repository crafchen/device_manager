# device_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Device Manager API",
      default_version='v1',
      description="API quản lý thiết bị & nhân viên",
      contact=openapi.Contact(email="your_email@example.com"),
   ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[],  # Bỏ mặc định, vì DRF sẽ dùng JWT
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # Swagger endpoints
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
