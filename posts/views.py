# from django.shortcuts import render
# from models import Post
# from django.contrib.auth.decorators import login_required
# from hashtags.model import Hashtag

# # Create your views here.
# from django.db import transaction

# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         content = request.POST['content']
#         hashtags = request.POST.get('hashtags', '').split(',')
        
#         with transaction.atomic():
#             post = Post.objects.create(user=request.user, content=content)
#             for hashtag_name in hashtags:
#                 hashtag_name = hashtag_name.strip()
#                 if hashtag_name:
#                     hashtag, _ = Hashtag.objects.get_or_create(name=hashtag_name)
#                     post.hashtags.add(hashtag)
        
