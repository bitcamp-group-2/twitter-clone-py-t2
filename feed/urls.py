from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feeds_view, name='feeds'),
]
