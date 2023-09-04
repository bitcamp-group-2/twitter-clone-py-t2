from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.feedList.as_view()),
    path('feed/<int:pk>/', views.feedDetail.as_view()),
]