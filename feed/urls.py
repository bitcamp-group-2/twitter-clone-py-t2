from django.urls import path, include
from . import views
from rest_framework import routers
from .views import FeedsAPIView


router = routers.DefaultRouter()
router.register(r'feed', views.FeedsAPIView, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
]
