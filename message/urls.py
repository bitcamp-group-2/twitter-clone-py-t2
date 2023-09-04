from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MessageListCreateView

router = DefaultRouter()
router.register(r'message', MessageListCreateView, basename='message')

urlpatterns = [
    # Other URL patterns may go here
    
    path('', include(router.urls)),
]
