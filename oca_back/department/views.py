from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Department
from .serializer import DepartmentSerializer
from oca_back.permissions import IsAdminOrReadOnly


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


class DepartmentList(APIView):
    """
        List all department, or create a new snippet.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, format=None):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
    """
    Retrieve, update or delete a department instance.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Department.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        department = self.get_object(pk)

        if department is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = DepartmentSerializer(department)
            response = Response(serializer.data)

        return response

    def put(self, request, pk, format=None):
        department = self.get_object(pk)

        if department is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = DepartmentSerializer(department, data=request.data)

            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data)

            else:
                response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response

    def delete(self, request, pk, format=None):
        department = self.get_object(pk)

        if department is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            department.delete()
            response = Response(status=status.HTTP_204_NO_CONTENT)

        return response
