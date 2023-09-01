from django.urls import path
from .views import CommentCreateView, CommentListView

urlpatterns = [
    path('comments/create/', CommentCreateView.as_view(), name='create-comment'),
    path('comments/list/', CommentListView.as_view(), name='comment-list'),
]
