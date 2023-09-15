from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class groups(models.Model):
    title = models.TextField(max_length=30)
    member_id = models.CharField(
        max_length=30,  blank=False, null=False, default=0)
    admin_id = models.CharField(
        max_length=30,  blank=False, null=False, default=0)


class AdminPermission(models.Model):
    class Meta:
        permissions = [
            ("can_post_and_delete", "Can post and delete"),
        ]
