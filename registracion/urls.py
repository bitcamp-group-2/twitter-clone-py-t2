
from django.urls import path
from .views import UserRegistrationView, UserLoginView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('', UserLoginView.as_view(), name='login'),
]
