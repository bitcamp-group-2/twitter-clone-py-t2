from models import Message
from rest_framework import serializers
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):
    sender = User(read_only=True)
    recipient = User(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'