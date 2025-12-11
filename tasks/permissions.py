from rest_framework import permissions
from django.contrib.auth.models import Group

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Admin').exists():
            return True
        return obj.owner == request.user

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Admin').exists()