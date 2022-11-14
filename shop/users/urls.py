from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.user_login, name = 'login'),
    path('registration', views.user_registration, name = 'registration'),
    path('logout', views.user_logout, name = 'logout'),
]
