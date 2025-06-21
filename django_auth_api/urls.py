from django.contrib import admin
from django.urls import path, include, re_path

from authapi.views import RedirectToLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authapi.urls')),
    path('accounts/', include('allauth.urls')),
    re_path(r'^(?!admin/|api/|accounts/).*$', RedirectToLogin.as_view(), name='catch_all'),
]
