from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, UserViewSet, RegisterView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)  # Admin-only

urlpatterns = [
    path('auth/register/', RegisterView.as_view()),
    path('', include(router.urls)),
]