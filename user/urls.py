from django.urls import path
from .views import create_user

urlpatterns = [
    path('registration/', create_user, name='registration')
]