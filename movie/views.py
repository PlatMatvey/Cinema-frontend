from django.shortcuts import render
import requests
# Create your views here.
def home(request):
    response_movies = requests.get("http://127.0.0.1:8080/movies/movie")
    movie_list = response_movies.json()
    response_carrousel = requests.get("http://127.0.0.1:8080/advertising/carrousel")
    carrousel = response_carrousel.json()
    response = requests.get("http://127.0.0.1:8080/movies/serials")
    serial_list = response.json()
    return render(request, 'movie/master.html', {
        "movie_list": movie_list,
        "carrousel": carrousel,
        "serial_list": serial_list
    })

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

def movie_detail(request, movie_id):
    response = requests.get(f"http://127.0.0.1:8080/movies/movie/{movie_id}")
    movie = response.json()
    return render(request, 'movie/deteil_movie.html', {'movie': movie})