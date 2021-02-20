from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Department
from .serializer import DepartmentSerializer


@api_view(['GET'])
def department_over_view(request):
    api_urls = {
        'List': '/departments/',
        'Detail View': '/departments/<int:pk>',
        'Create': '/departments/',
        'Update': '/departments/<int:pk>',
        'Delete': '/departments/<int:pk>',
    }

    return Response(api_urls)


@api_view(['GET', 'POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_root(request, format=None):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print(request.data)
        return Response({"message": "Got some data!", "data": request.data})
