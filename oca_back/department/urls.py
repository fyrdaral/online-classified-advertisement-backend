from django.urls import path
from . import views as dept_view

urlpatterns = [
    path('', dept_view.user_root),
]
