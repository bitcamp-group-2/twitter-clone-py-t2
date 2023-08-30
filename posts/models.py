from django.db import models
from django.contrib.auth.models import User
from hashtags.model import Hashtag

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='posts')

    def __str__(self):
        return (f"{self.user} - {self.title}")
