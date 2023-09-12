from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Feed_List
from .serializers import feed_List_Serializer


class FeedsAPIView(viewsets.ModelViewSet):
    queryset = Feed_List.objects.all()
    serializer_class = feed_List_Serializer

    def get(self):
        posts = Feed_List.objects.order_by(
            '-created_at')[:3]  # Get the latest three posts
        serializer = feed_List_Serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
