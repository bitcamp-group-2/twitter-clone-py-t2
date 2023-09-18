from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikeViews

router = DefaultRouter()

router.register(r'', LikeViews)

urlpatterns = [
    path('', include(router.urls)),
]
