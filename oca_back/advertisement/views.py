from django.shortcuts import render
from django.urls import path
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Advertisement
from .serializer import AdvertisementSerializer
from oca_back.permissions import IsAuthenticatedOrReadCreateOnly


@api_view(['GET'])
def advertisement_over_view(request):
    api_urls = {
        'List': '/ads/',
        'Detail View': '/ads/<int:pk>',
        'Create': '/ads/',
        'Update': '/ads/<int:pk>',
        'Delete': '/ads/<int:pk>',
    }

    return Response(api_urls)


class AdvertisementList(APIView):
    """
        Get all ads and create an ad.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadCreateOnly]

    def get(self, request, format=None):
        advertisement = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisement, many=True)
        return Response(serializer.data)

    def post(self, request,  format=None):
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdvertisementDetail(APIView):
    """
    Retrieve, update or delete a department instance.
    """
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadCreateOnly]

    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return None

    def get(self, request, pk, format=None):
        advertisement = self.get_object(pk)

        if advertisement is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = AdvertisementSerializer(advertisement)
            response = Response(serializer.data)

        return response

    def put(self, request, pk, format=None):
        advertisement = self.get_object(pk)

        if advertisement is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            serializer = AdvertisementSerializer(advertisement, data=request.data)

            if serializer.is_valid():
                serializer.save()
                response = Response(serializer.data)

            else:
                response = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response

    def delete(self, request, pk, format=None):
        advertisement = self.get_object(pk)

        if advertisement is None:
            response = Response(status=status.HTTP_404_NOT_FOUND)

        else:
            advertisement.delete()
            response = Response(status=status.HTTP_204_NO_CONTENT)

        return response
