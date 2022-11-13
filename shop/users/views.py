from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

from users.admin import UserCreationForm, LoginForm

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request, 'users/login.html', {'form': form, 'error_maessage': 'Неверный логин или пароль'})
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def user_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.is_password_correct(request, form):
                form.save()
                cd = form.cleaned_data
                user = authenticate(email=cd['email'], password=cd['password1'])
                login(request, user)
                return HttpResponseRedirect("/")
            else:
                return render(request, 'users/registration.html', {'form': form, 'error_maessage': 'Слишком простой пароль или пароли не совпадают'})
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/")
