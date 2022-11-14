from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('filtred', views.filtred, name = 'filtred'),
    path('<str:product_name>', views.product_page, name = 'product_page'),
]
