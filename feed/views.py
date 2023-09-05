from django.shortcuts import render
from .models import PostFeeds


def feeds_view(request):
    posts = PostFeeds.objects.all().order_by('-created_at')
    return render(request, PostFeeds, {'posts': posts})
