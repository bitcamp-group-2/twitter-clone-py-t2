from django.urls import path , include
from .views import CommentCreateView, CommentListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'create', CommentCreateView, basename='create' ),
router.register (r'list', CommentListView, basename='list'),




urlpatterns =[
    path('', include(router.urls))
]