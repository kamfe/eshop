from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(('users.urls', 'users'), namespace='users')),
    path('cart', include(('cart.urls', 'cart'), namespace='cart')),
    path('orders', include(('orders.urls', 'orders'), namespace='orders')),
    path('', include('main.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
