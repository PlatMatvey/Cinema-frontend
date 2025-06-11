from django.urls import path
from .views import create_user, login_view
from . import views

urlpatterns = [
    path('registration/', create_user, name='registration'),
    path('login/', login_view, name='login'),
    path('profile/<int:user_id>/', views.user_profile, name='profile'),
    path('movie/<int:movie_id>/review/', views.review_movie, name='review_movie'),
    path('movie/<int:movie_id>/rating/', views.rating_movie, name='rating_movie'),
    path('movie/<int:serial_id>/review/', views.review_serial, name='review_serial'),
    path('movie/<int:serial_id>/rating/', views.rating_serial, name='rating_serial'),
]