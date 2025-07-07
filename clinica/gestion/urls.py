from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import register_user

urlpatterns = [
    path('api/register/', register_user, name='api_register'),
    path('api/login/', TokenObtainPairView.as_view(), name='api_login'),
]