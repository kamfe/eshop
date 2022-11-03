from django.shortcuts import render

def index(request):
    data = {
        'title': 'Топовые процессоры по низким ценам',
    }
    return render(request, 'main/index.html', data)

def login(request):
    data = {
        'title': 'Вход в аккаунт',
    }
    return render(request, 'main/login.html', data)

def registration(request):
    data = {
        'title': 'Регистрация :)',
    }
    return render(request, 'main/registration.html', data)
