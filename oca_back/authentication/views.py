from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def auth_over_view(request):
    api_urls = {
        'Get Token': '/authentication/',
        'Refresh Token': '/authentication/refresh/',
    }

    return Response(api_urls)
