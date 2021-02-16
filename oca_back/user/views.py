from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer


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


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)
