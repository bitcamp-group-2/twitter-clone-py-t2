from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.groupsList.as_view()),
    path('groups/<int:pk>/', views.groupsDetail.as_view()),
]