from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from tasks.models import Task

class Command(BaseCommand):
    help = 'Create Admin and User roles'

    def handle(self, *args, **options):
        # Create groups
        admin_group, created = Group.objects.get_or_create(name='Admin')
        user_group, created = Group.objects.get_or_create(name='User')

        # Permissions for Task model
        content_type = ContentType.objects.get_for_model(Task)
        permissions = Permission.objects.filter(content_type=content_type)

        # Admin gets all permissions
        admin_group.permissions.set(permissions)

        # User gets only view, change, add, delete for own tasks (handled in views)
        user_group.permissions.set([])  # We'll enforce in custom perms

        self.stdout.write(self.style.SUCCESS('Roles created successfully'))