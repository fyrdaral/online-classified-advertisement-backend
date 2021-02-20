from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import User
from .serializer import UserSerializer, UserMiniSerializer, UserCreateSerializer
from oca_back.permissions import IsAuthenticatedOrReadCreateOnly

@api_view(['GET'])
def user_over_view(request):
    api_urls = {
        'List': '/users/',
        'Detail View': '/users/<int:pk>',
        'Create': '/users/',
        'Update': '/users/<int:pk>',
        'Delete': '/users/<int:pk>',
    }

    return Response(api_urls)


class UserList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadCreateOnly]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserMiniSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadCreateOnly]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        user = self.get_object(pk)

        if user is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        elif (request.user and
              request.user.is_authenticated and
              pk == request.user.id):
            serializer = UserSerializer(user)
            response = Response(serializer.data)
        else:
            serializer = UserMiniSerializer(user)
            response = Response(serializer.data)
        return response

    def put(self, request, pk, format=None):
        user = self.get_object(pk)

        if user is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = UserSerializer(user, data=request.data)

            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data)

            else:
                response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)

        if user is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            user.delete()
            response = Response(status=status.HTTP_204_NO_CONTENT)

        return response
