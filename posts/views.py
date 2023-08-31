from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.decorators import login_required
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    @login_required
    def create_post(self, request):
        content = request.data.get('content')
        post = request.save(user=self.request.user)
        # hashtags = request.data.get('hashtags', '').split(',')

        # Your logic for creating the post and adding hashtags goes here

        return Response({'success': True}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['POST'])
    @login_required
    def create_with_hashtags(self, request):
        content = request.data.get('content')
        # hashtags = request.data.get('hashtags', '').split(',')

        # Your logic for creating the post and adding hashtags goes here

        return Response({'success': True}, status=status.HTTP_201_CREATED)