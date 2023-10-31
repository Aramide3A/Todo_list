from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import *
from rest_framework.permissions import AllowAny
# Create your views here.

class ApiOverview(APIView):
    def get(self, request):
        routes = [
        {
            'Endpoint': '/signup',
            'method': 'POST',
            'body': 'username, first_name, last_name,email, password',
            'description': 'FOR SIGNUP'
        },
        {
            'Endpoint': '/login',
            'method': 'POST',
            'body': 'username,password',
            'description': 'FOR LOGIN'
        },
        {
            'Endpoint': '/create',
            'method': 'POST',
            'body': 'task, description, completed',
            'description': 'FOR Creating NEW TASKS'
        },
        {
            'Endpoint': '/tasklist',
            'method': 'GET',
            'body': None,
            'description': 'FOR GETTING LIST OF ALL TASKS'
        },
        ]
        return Response(routes)
    
class Signup(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user = user)
            return Response({'Signup successful'})
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class Login(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        user = get_object_or_404(User, username = request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({'detail not found'}, status = status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key})
    
class All_Task(APIView):
    def get(self, request):
        tasks = Todo_list.objects.all()
        serializer = TodoSerializer(tasks, many = True)
        return Response(serializer.data)

class Create_task(APIView):
    def post(self, request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class Update_task(APIView):
    def put(self, request, pk):
        instance = Todo_list.objects.get(id = pk)
        serializer = TodoSerializer(instance, data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class Delete_task(APIView):
    def delete(self, request, pk):
        task = Todo_list.objects.get(id = pk)
        task.delete()
        return Response({'task deleted'})
    
class Logout(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
