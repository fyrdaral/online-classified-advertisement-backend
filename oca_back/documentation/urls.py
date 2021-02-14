from django.urls import path
from . import views
from user import views as user_view
from authentication import views as auth_view

urlpatterns = [
    path('', views.api_over_view, name='API Overview'),
    path('users/', user_view.user_over_view, name='Users Overview'),
    path('authentication/', auth_view.auth_over_view, name='Authenticate Overview'),
]