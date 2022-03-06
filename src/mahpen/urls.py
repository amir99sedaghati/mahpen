"""mahpen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/__debug__/', include('debug_toolbar.urls')),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/content/', include('course.urls')),
    path('api/zarin/', include('zarinpal.urls')),
    path('api/user/', include('user_management.urls')),
    path('api/user/get-token/', views.obtain_auth_token),
    path('api/', get_schema_view(
        title="mahpen APIs",
        description="API for all things ......",
        version="1.0.0"
    ), name='mahpen-schema'),
]

#

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import re_path

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]