from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

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


@api_view(['GET'])
def user_list(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)

    return Response(serializer.data)
