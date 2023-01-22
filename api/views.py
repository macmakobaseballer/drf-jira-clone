from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, permissions, generics,viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, ProfileSerializer, TaskSerializer
from .models import Task, Category, Profile
from . import custompermissions

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny)

class ListUsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed.'}
        return Response(response, status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed.'}
        return Response(response, status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        response = {'message': 'DELETE method is not allowed.'}
        return Response(response, status.HTTP_400_BAD_REQUEST)

    def update(self, request,*args,**kwargs):
        response = {'message': 'PUT method is not allowed.'}
        return Response(response, status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed.'}
        return Response(response, status.HTTP_400_BAD_REQUEST)

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticated, custompermissions.OwnerPermission,)

    def create(self, serializer):
        serializer.save(owner=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed.'}
        return Response(response, status.HTTP_400_BAD_REQUEST)

