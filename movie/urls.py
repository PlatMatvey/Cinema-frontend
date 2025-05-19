from django.urls import path
from .views import home, list_movie, list_serials

urlpatterns = [
    path('', home),
    path('movies/', list_movie),
    path('serials/', list_serials),
]