from django.shortcuts import render
import requests
# Create your views here.
def list_movie(request):
    response = requests.get("http://127.0.0.1:8080/movies/movie")
    move_list = response.json()
    print(move_list)
    return render(request, 'movie/master.html', {"move_list": move_list} )

def carrousel(request):
    response = requests.get("http://127.0.0.1:8080/advertising/carrousel")
    carrousel = response.json()
    print(carrousel)
    return render(request, 'movie/carrousel.html', {"carrousel": carrousel})