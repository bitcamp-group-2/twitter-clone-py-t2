from django.shortcuts import render
from .serializers import LikeSerializer
from rest_framework import viewsets
from .models import Like
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

class LikeViews(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    @action(detail=True, methods=['POST'])
    def create_like(self, request, pk=None):
        instance = get_object_or_404(Like, pk=pk)

        existing_like = Like.objects.filter(user=request.user, liked_item=instance).first()

        like = Like.objects.create(user=request.user, liked_item=instance)

        serializer = LikeSerializer(like)
        