from rest_framework import serializers
from .models import PostFeeds


class groupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostFeeds
        fields = ["id", "user", "content", "created_at"]
