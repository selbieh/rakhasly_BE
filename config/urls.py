from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from config import settings
from django.conf.urls.static import static
from rest_framework.permissions import AllowAny
from dj_rest_auth.views import PasswordResetView, PasswordResetConfirmView

from config.views import custom_reset_handler_submit, custom_confirm, custom_reset_handler

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
    path('auth/registration/account-confirm-email/<str:key>/', custom_confirm),

    path('api/v1/', include('apps.driver_license_orders.urls')),
    path('api/v1/', include('apps.car_license_orders.urls')),
    path('api/v1/', include('apps.users.urls')),
    path('api/v1/', include('apps.ratings.urls')),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # Password Reset URLs
    path('auth/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('dj-rest-auth/custom_reset_handler_submit/', custom_reset_handler_submit, name='custom_reset_handler_submit'),
    path('auth/reset/confirm/<str:uid>/<str:token>/', custom_reset_handler, name='password_reset_confirm'),
    # yasq (swagger)
    path('api/swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

