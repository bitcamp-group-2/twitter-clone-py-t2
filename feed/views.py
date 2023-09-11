from django.shortcuts import render
from .models import Feed_List


def feeds_view(request):
    posts = Feed_List.objects.order_by(
        '-created_at')[:3]  # Get the latest three tweets
    return render(request, Feed_List, {'posts': posts})
