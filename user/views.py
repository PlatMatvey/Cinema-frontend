import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm, ReviewForm, RatingForm, CreateChatForm


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post('http://127.0.0.1:8080/registration/registrations/', json=data)
            if response.status_code == 201:
                return HttpResponse("Успешно отправлено!")
            else:
                return HttpResponse("Ошибка при отправке", status=500)
    else:
        form = RegisterForm()
    return render(request, 'user/registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        response = requests.post('http://127.0.0.1:8080/api/token/', json={
            'username': username,
            'password': password
        })
        if response.status_code == 200:
            token_data = response.json()
            request.session['access_token'] = token_data['access']
            request.session['refresh_token'] = token_data['refresh']
            return redirect('master')
        return HttpResponse("Неверный логин или пароль", status=401)
    return render(request, 'user/login.html')

@login_required
def review_movie(request, movie_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            data['movie'] = movie_id
            data['user'] = [request.user.id]
            access_token = request.session.get('access_token')

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            response = requests.post('http://127.0.0.1:8080/mark/review_movie/', json=data, headers=headers)

            print("Response status:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 201:
                return HttpResponse("Комментарий успешно отправлен!")
            else:
                return HttpResponse("Ошибка при отправке комментария", status=500)
    else:
        form = ReviewForm()

    return render(request, 'mark/review_movie.html', {'form': form})

@login_required
def rating_movie(request, movie_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['movie'] = movie_id
            access_token = request.session.get('access_token')

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post('http://127.0.0.1:8080/mark/rating_movie/', json=data, headers=headers)

            print("Response status:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 201:
                return HttpResponse("Рейтинг успешно отправлен!")
            else:
                return HttpResponse("Ошибка при отправке рейтинга", status=500)
    else:
        form = RatingForm()

    return render(request, 'mark/rating_movie.html', {'form': form})

@login_required
def review_serial(request, serial_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            data['serial'] = serial_id
            data['user'] = [request.user.id]
            access_token = request.session.get('access_token')

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }

            response = requests.post('http://127.0.0.1:8080/mark/review_serial/', json=data, headers=headers)

            print("Response status:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 201:
                return HttpResponse("Комментарий успешно отправлен!")
            else:
                return HttpResponse("Ошибка при отправке комментария", status=500)
    else:
        form = ReviewForm()

    return render(request, 'mark/review_serial.html', {'form': form})

@login_required
def rating_serial(request, serial_id):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['serial'] = serial_id
            access_token = request.session.get('access_token')

            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json'
            }
            response = requests.post('http://127.0.0.1:8080/mark/rating_serial/', json=data, headers=headers)

            print("Response status:", response.status_code)
            print("Response text:", response.text)

            if response.status_code == 201:
                return HttpResponse("Рейтинг успешно отправлен!")
            else:
                return HttpResponse("Ошибка при отправке рейтинга", status=500)
    else:
        form = RatingForm()

    return render(request, 'mark/rating_serial.html', {'form': form})

def create_chat(request):
    if request.method == 'POST':
        form = CreateChatForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post('http://127.0.0.1:8080/message/chat/', json=data)
            if response.status_code == 201:
                return HttpResponse("Успешно создано!")
            else:
                return HttpResponse(f"Ошибка API: {response.status_code}", status=500)
    else:
        form = CreateChatForm()
        all_users = requests.get('http://127.0.0.1:8080/registration/registrations/')
        users = all_users.json()
        print(users)

        return render(request, 'chat/create_chat.html', {
            'form': form,
            'users': users,
        })
