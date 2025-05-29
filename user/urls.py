from django.urls import path
from .views import create_user, login_view

urlpatterns = [
    path('registration/', create_user, name='registration'),
    path('login/', login_view, name='login')
]