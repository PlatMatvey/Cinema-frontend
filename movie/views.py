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
    serial_list = response.json()[:4]
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
    genres_set = set()
    for m in movie_all:
        raw = m.get('genre', '')
        for g in raw.split(','):
            g = g.strip()
            if g:
                genres_set.add(g)
    all_genres = sorted(genres_set)
    selected_genres = request.GET.getlist('genre')
    selected_formats = request.GET.getlist('format')
    if selected_genres:
        def has_genre(m):
            parts = [x.strip() for x in m.get('genre', '').split(',')]
            return any(g in parts for g in selected_genres)
        movie_all = [m for m in movie_all if has_genre(m)]
    if selected_formats:
        movie_all = [m for m in movie_all if m.get('format') in selected_formats]
    return render(request, 'movie/all_movie.html', {
        'movie_all': movie_all,
        'all_genres': all_genres,
        'selected_genres': selected_genres,
        'selected_formats': selected_formats,
    })

def all_serials(request):
    response = requests.get("http://127.0.0.1:8080/movies/serials")
    serial_all = response.json()
    genres_set = set()
    for m in serial_all:
        raw = m.get('genre', '')
        for g in raw.split(','):
            g = g.strip()
            if g:
                genres_set.add(g)
    all_genres = sorted(genres_set)
    selected_genres = request.GET.getlist('genre')
    selected_formats = request.GET.getlist('format')
    if selected_genres:
        def has_genre(m):
            parts = [x.strip() for x in m.get('genre', '').split(',')]
            return any(g in parts for g in selected_genres)

        serial_all = [m for m in serial_all if has_genre(m)]
    if selected_formats:
        serial_all = [m for m in serial_all if m.get('format') in selected_formats]
    return render(request, 'movie/all_serial.html', {
        'serial_all': serial_all,
        'all_genres': all_genres,
        'selected_genres': selected_genres,
        'selected_formats': selected_formats,
    })
