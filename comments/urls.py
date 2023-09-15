from django.urls import path , include
from .views import CommentCreateView, CommentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'comments/create', CommentCreateView, basename='create' ),
router.register (r'comments/list', CommentListView, basename='list'),




urlpatterns =[
    path('', include(router.urls))
]