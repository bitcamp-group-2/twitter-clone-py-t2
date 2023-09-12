from django.urls import path, include
from . import views
from rest_framework import routers
from .views import groupsList


router = routers.DefaultRouter()
router.register(r'groups', views.groupsList, basename='groups')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]
