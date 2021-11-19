from django.contrib import admin
from django.urls import path, include
from django.http.response import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    # User management
    path('users/', include('user_management.urls')),

    # Healthcheck
    path(r'healthcheck/', lambda r: HttpResponse())
]
