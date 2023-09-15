from django.shortcuts import render
from .models import Message
from .serializers import MessageSerializer
from rest_framework import viewsets, permissions

# Create your views here.

class MessageListCreateView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def message_create(self, serializer):
        serializer.save(sender=self.request.user)