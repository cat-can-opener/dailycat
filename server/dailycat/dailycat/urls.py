import os

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Dailycat',
        default_version='v1',
        description='Show cat photo and create name!',
        contact=openapi.Contact(email='bartkim0426@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

api_urls = [
    path("", include("cats.urls", namespace="cats")),
    path("", include("rest_auth.urls")),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path("api/v1/", include(api_urls)),
    # path("", include("cats.urls", namespace="cat_test")),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('user/signup/', include('rest_auth.registration.urls'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
