from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Comment(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    post_id = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.user_id.username} on Post {self.post_id.id}"


