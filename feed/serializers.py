from rest_framework import serializers
from .models import feed

class feedSerializer(serializers.ModelSerializer):
    class Meta:
        model = feed
        fields = []     #"id", "title", "member_id", "admin_id"