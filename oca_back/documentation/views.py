from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_over_view(request):
    api_urls = {
        'Authentication': '/authentication/',
        'Users': '/users/',
        'Departments': '/departments/',
    }

    return Response(api_urls)
