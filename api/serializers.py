from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password']

class TodoSerializer(serializers.ModelSerializer):
    class Meta():
        model = Todo_list
        fields = '__all__'