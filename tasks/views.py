from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication  # add this import at top
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Task
from .serializers import TaskSerializer
from .permissions import IsOwnerOrAdmin, IsAdmin
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    authentication_classes = (JWTAuthentication, SessionAuthentication)  # ← ADD THIS LINE
    # filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['status', 'owner']  # Bonus: filters
    # search_fields = ['title', 'description']  # Bonus: search
    # ordering_fields = ['created_at', 'updated_at']  # Bonus: sort

    def get_queryset(self):
        if self.request.user.groups.filter(name='Admin').exists():
            return Task.objects.all()
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['patch'])
    def toggle_status(self, request, pk=None):
        task = self.get_object()
        task.status = not task.status
        task.save()
        return Response(TaskSerializer(task).data)

# Admin-only view for listing users (bonus)
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().select_related('groups')
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# class RegisterView(APIView):
#     permission_classes = [AllowAny]        # ← ADD THIS LINE
#     authentication_classes = []            # ← ADD THIS LINE (optional but clean)

#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def api_root(request):
    return Response({
        'message': 'Welcome to Task Manager API!',
        'endpoints': {
            'auth': {
                'register': 'POST /api/auth/register/',
                'login': 'POST /api/auth/token/',
                'refresh': 'POST /api/auth/token/refresh/',
            },
            'tasks': {
                'list_create': 'GET/POST /api/tasks/',
                'detail': 'GET/PUT/DELETE /api/tasks/{id}/',
                'toggle_status': 'PATCH /api/tasks/{id}/toggle_status/',
            },
            'admin': 'GET /admin/ (Django Admin)',
        },
        'debug': 'Use tools like Postman for testing with JWT tokens.',
    })