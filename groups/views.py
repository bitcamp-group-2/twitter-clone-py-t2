from django.shortcuts import render
from rest_framework import generics
from .models import groups
from .serializers import groupsSerializer

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from .models import AdminPermission  # your model
from rest_framework import viewsets

# Create your views here.


class groupsList(viewsets.ModelViewSet):
    queryset = groups.objects.all()
    serializer_class = groupsSerializer


class groupsDetail(viewsets.ModelViewSet):
    queryset = groups.objects.all()
    serializer_class = groupsSerializer


@permission_required("groups.can_post_and_delete")
def post_or_delete_view(request, pk):
    obj = get_object_or_404(AdminPermission, pk=pk)

    if request.method == "POST":
        # Handle POST request
        # Your code here
        return JsonResponse({"message": "POST request handled."})

    elif request.method == "DELETE":
        # Handle DELETE request
        # Your code here
        return JsonResponse({"message": "DELETE request handled."})
