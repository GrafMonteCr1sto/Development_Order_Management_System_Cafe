from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

# Импортируем необходимые компоненты из Django REST Framework
from rest_framework.routers import DefaultRouter
from orders.views_api import OrderViewSet

# Создаем маршрутизатор для API
router = DefaultRouter()
# Регистрируем маршрут для работы с заказами через API
router.register(r'orders', OrderViewSet)

# Список URL-шаблонов для проекта
urlpatterns = [
    path('admin/', admin.site.urls),  # Маршрут для административного интерфейса Django
    path('orders/', include('orders.urls')),  # Включаем URL-шаблоны из приложения orders
    path('api/', include(router.urls)),  # Включаем маршруты API, определенные в маршрутизаторе
    path('', RedirectView.as_view(url='/orders/', permanent=True)),  # Перенаправление с корневого URL на /orders/
]