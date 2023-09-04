from django.db import models

# Create your models here.

class feed(models.Model):
    title = models.TextField(max_length=30)
    member_id = models.CharField(max_length=30,  blank=False, null=False, default=0)
    admin_id = models.CharField(max_length=30,  blank=False, null=False, default=0)