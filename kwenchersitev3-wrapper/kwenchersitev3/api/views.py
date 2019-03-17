from django.shortcuts import render
from rest_framework import  serializers, viewsets, generics, filters
from django.contrib.auth.models import User
from serializers import *

# Create your views here.
#ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer