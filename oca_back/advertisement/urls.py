from django.urls import path
from .views import AdvertisementList, AdvertisementDetail

urlpatterns = [
    path('', AdvertisementList.as_view()),
    path('<int:pk>/', AdvertisementDetail.as_view()),
]
