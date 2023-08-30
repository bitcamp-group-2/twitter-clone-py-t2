
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .serializers import RegistrationSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# This function for User-registration.
@api_view(["POST"])
@permission_classes([AllowAny])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        user_ser = serializer.save()
        user = User.objects.get(username = request.data["username"])
        user.set_password(request.data["password"])
        token = Token.objects.create(user = user)
        user.save()
        return Response({"message": "Registration successful."}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#This function for LogIn.
@api_view(["POST"])
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    user = authenticate(username=username, password=password)
    
    if user is not None:
        if user.is_active:
            login(request, user)  # For session-based authentication
            token, created = Token.objects.get_or_create(user=user)  # For token-based authentication
            serializer = RegistrationSerializer(instance = user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "User account is disabled."}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    



@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_logout(request):
    logout(request)  # For session-based authentication
    request.auth.delete()  # For token-based authentication
    return Response({"message": "Logout successful."}, status=status.HTTP_200_OK)