import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
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
            tokens = response.json()
            access = tokens.get('access')
            refresh = tokens.get('refresh')
            # Сохраняем токены в сессии что бы мы могли Матвей обращаться в защищённые вюшки
            request.session['access_token'] = access
            request.session['refresh_token'] = refresh
            return redirect('master')
        return HttpResponse("Неверный логин или пароль", status=401)
    return render(request, 'user/login.html')


# def dashboard_view(request):
#     token = request.session.get('access_token')
#     # Получаем токен
#     if not token:
#         return redirect('login')
#     headers = {
#         'Authorization': f'Bearer {token}'
#     }
#     response = requests.get('http://127.0.0.1:8000/api/some_protected/', headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#         return render(request, 'dashboard.html', {'data': data})
#     else:
#         return HttpResponse("Ошибка доступа", status=403)