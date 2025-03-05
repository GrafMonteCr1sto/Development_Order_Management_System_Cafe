# cafe_order_system_manager/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from rest_framework.routers import DefaultRouter
from orders.views_api import OrderViewSet

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls')),
    path('api/', include(router.urls)),
    path('', RedirectView.as_view(url='/orders/', permanent=True)),  # Добавляем перенаправление на /orders/
]