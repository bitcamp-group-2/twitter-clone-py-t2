from rest_framework import serializers
from .models import Feed_List


class feed_List_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Feed_List
        # Serialize all fields in the model
        fields = ["id", "user", "content", "created_at"]
