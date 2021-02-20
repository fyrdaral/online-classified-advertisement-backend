from django.urls import path
# from . import views as dept_view
from .views import DepartmentList, DepartmentDetail

urlpatterns = [
    path('', DepartmentList.as_view()),
    path('<int:pk>/', DepartmentDetail.as_view())
]
