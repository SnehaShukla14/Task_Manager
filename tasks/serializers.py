from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Task
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}   # important!

    def create(self, validated_data):
        # This line properly hashes the password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Automatically add new user to the "User" group
        from django.contrib.auth.models import Group
        user_group, _ = Group.objects.get_or_create(name='User')
        user.groups.add(user_group)
        return user
    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         # Assign default 'User' role
#         user.groups.add(Group.objects.get(name='User'))
#         return user

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'created_at', 'updated_at', 'owner']
        read_only_fields = ['created_at', 'updated_at', 'owner']