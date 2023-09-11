from rest_framework import serializers
from .models import Feed_List


class feed_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_List
        fields = ["id", "user", "content", "created_at"]
