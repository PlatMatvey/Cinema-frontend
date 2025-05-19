from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    response = requests.get("http://127.0.0.1:8080/advertising/carrousel")
    carrousel = response.json()
    print(carrousel)
    return render(request, 'movie/master.html',{"carrousel": carrousel})

def list_movie(request):
    response = requests.get("http://127.0.0.1:8080/movies/movie")
    movie_list = response.json()
    print(movie_list)
    return render(request, 'movie/list_movie.html', {"movie_list": movie_list} )

def list_serials(request):
    response = requests.get("http://127.0.0.1:8080/movies/serials")
    serial_list = response.json()
    print(serial_list)
    return render(request, 'movie/list_serial.html', {"serial_list": serial_list})

def carrousel(request):
    response = requests.get("http://127.0.0.1:8080/advertising/carrousel")
    carrousel = response.json()
    print(carrousel)
    return render(request, 'movie/carrousel.html', {"carrousel": carrousel})