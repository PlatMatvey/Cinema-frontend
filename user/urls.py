from django.urls import path
from .views import create_user, login_view
from . import views

urlpatterns = [
    path('registration/', create_user, name='registration'),
    path('login/', login_view, name='login'),
    path('movie/<int:movie_id>/review/', views.add_review, name='add_review'),
    path('movie/<int:movie_id>/rating/', views.add_rating, name='add_rating'),
    # path('chat/send/', views.send_message, name='send_message'),
    # path('chat/create/', views.create_chat, name='create_chat'),
]