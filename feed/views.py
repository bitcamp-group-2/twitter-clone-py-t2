from django.shortcuts import render
from rest_framework import generics
from .models import feed
from .serializers import feedSerializer

# Create your views here.
class feedList(generics.ListCreateAPIView):
    queryset = feed.objects.all()
    serializer_class = feedSerializer

class feedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = feed.objects.all()
    serializer_class = feedSerializer