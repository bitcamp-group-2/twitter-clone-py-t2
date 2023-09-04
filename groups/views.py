from django.shortcuts import render
from rest_framework import generics
from .models import groups
from .serializers import groupsSerializer

# Create your views here.
class groupsList(generics.ListCreateAPIView):
    queryset = groups.objects.all()
    serializer_class = groupsSerializer

class groupsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = groups.objects.all()
    serializer_class = groupsSerializer