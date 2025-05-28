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
    movie_list = response.json()[:4]
    print(movie_list)
    return render(request, 'movie/list_movie.html', {"movie_list": movie_list} )

def list_serials(request):
    response = requests.get("http://127.0.0.1:8080/movies/serials")
    serial_list = response.json()
    print(serial_list)
    return render(request, 'movie/list_serials.html', {"serial_list": serial_list})

def movie_detail(request, movie_id):
    response = requests.get(f"http://127.0.0.1:8080/movies/movie/{movie_id}")
    movie = response.json()
    return render(request, 'movie/deteil_movie.html', {'movie': movie})

def serial_detail(request, serial_id):
    response = requests.get(f"http://127.0.0.1:8080/movies/serials/{serial_id}")
    serial = response.json()
    return render(request, 'movie/detail_serial.html', {'serial': serial})

def all_movie(request):
    response = requests.get("http://127.0.0.1:8080/movies/movie")
    movie_all = response.json()
    selected_genre = request.GET.getlist('genre')
    selected_format = request.GET.getlist('format')
    def movie_filter(n):
        if selected_genre and n.get('genre') not in selected_genre:
            return False
        if selected_format and n.get('format') not in selected_format:
            return False
        return True
    filtered = [n for n in movie_all if movie_filter(n)]
    return render(request, 'movie/all_movie.html', {
        'movie_all': filtered,
        'selected_genre': selected_genre,
        'selected_format': selected_format,
    })

def all_serials(request):
    response = requests.get("http://127.0.0.1:8080/movies/serials")
    serial_all = response.json()
    selected_genre = request.GET.getlist('genre')
    selected_format = request.GET.getlist('format')
    def serial_filter(n):
        if selected_genre and n.get('genre') not in selected_genre:
            return False
        if selected_format and n.get('format') not in selected_format:
            return False
        return True
    filtered = [n for n in serial_all if serial_filter(n)]
    return render(request, 'movie/all_serial.html', {
        'serial_all': filtered,
        'selected_genre': selected_genre,
        'selected_format': selected_format,
    })