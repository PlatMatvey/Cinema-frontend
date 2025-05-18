from django.urls import path
from .views import home, list_movie, list_serials, carrousel

urlpatterns = [
    path('home/', home),
    path('movies/', list_movie),
    path('serials/', list_serials),
    path('carrousel/', carrousel)
]