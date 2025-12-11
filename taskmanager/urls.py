"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tasks.views import api_root  # Add this import

urlpatterns = [
    path('', api_root, name='api_root'),  # <-- Add this for root /
    path('admin/', admin.site.urls),
    # JWT Auth Endpoints (manual wiring)
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh
    path('api/', include('tasks.urls')),  # Your app URLs (tasks, register, etc.)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # ← ADD this line
]