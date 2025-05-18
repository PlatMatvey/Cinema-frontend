import requests
from django.http import HttpResponse
from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            response = requests.post('Апишка', json=data)
            if response.status_code == 200:
                return HttpResponse("Успешно отправлено!")
            else:
                return HttpResponse("Ошибка при отправке", status=500)
    else:
        form = RegisterForm()
    return render(request, 'user/registration.html', {'form': form})