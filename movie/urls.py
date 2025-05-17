from django.urls import path
from .views import list_movie, carrousel

urlpatterns = [
    path('', list_movie),
    path('carrousel/', carrousel)
]