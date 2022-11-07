from django.urls import path
from . import views
from users import views as userviews

urlpatterns = [
    path('', views.index, name = 'home'),
    path('login', userviews.user_login, name = 'login'),
    path('registration', userviews.user_registration, name = 'registration'),
    path('logout', userviews.user_logout, name = 'logout')
]
