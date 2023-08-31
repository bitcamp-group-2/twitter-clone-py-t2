from django.shortcuts import render
from models import Message
from serializers import MessageSerializer
from rest_framework import generics, permissions

# Create your views here.

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def message_create(self, serializer):
        serializer.save(sender=self.request.user)