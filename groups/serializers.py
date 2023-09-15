from rest_framework import serializers
from .models import groups

class groupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = groups
        fields = ["id", "title", "member_id", "admin_id"]