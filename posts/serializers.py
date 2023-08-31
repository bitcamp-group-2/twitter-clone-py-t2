from rest_framework import serializers
from .models import Post
# from hashtags.serializers import HashtagSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['user', 'title']

        # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
    


# class PostSerializer(serializers.ModelSerializer):
#     hashtags = HashtagSerializer(many=True, read_only=True, required=False)


#     class Meta:
#         model = Post
#         fields = ["content", "hashtags"]