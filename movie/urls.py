from django.urls import path
from .views import home, list_movie, list_serials
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('movies/', list_movie),
    path('serials/', list_serials),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail')
]