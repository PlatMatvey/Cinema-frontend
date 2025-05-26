from django.urls import path
from .views import home, list_movie, list_serials, all_movie
from . import views

urlpatterns = [
    path('', home, name='master'),
    path('movie/', list_movie),
    path('serials/', list_serials),
    path('movies/', all_movie, name='all_movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('serials/<int:serial_id>/', views.serial_detail, name='serial_detail')
]