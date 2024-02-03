from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny

# from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

# from config.settings import SPECTACULAR_SETTINGS

# yasq configuration
schema_view = get_schema_view(
   openapi.Info(
      title="NOS_backend_service API",
      default_version='1.0.0',
      description="Documentation of API endpoints of NOS_backend_service",
   ),
    url="",
    public=True,
    permission_classes=[
        AllowAny,
    ],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.driver_license_orders.urls')),
    path('api/v1/', include('apps.car_license_orders.urls')),
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/', include('apps.ratings.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),


    # path('api/schema/', SpectacularAPIView.as_view()),
    # path('api/docs/', SpectacularSwaggerView.as_view()),

    # yasq (swagger)
    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

