from django.urls import path
from . import views

# Список URL-шаблонов для представлений, связанных с заказами
urlpatterns = [
    # Маршрут для отображения списка заказов
    path('', views.order_list, name='order_list'),

    # Маршрут для создания нового заказа
    path('create/', views.order_create, name='order_create'),

    # Маршрут для обновления существующего заказа
    # <int:pk> указывает на то, что это целочисленный параметр, представляющий первичный ключ заказа
    path('update/<int:pk>/', views.order_update, name='order_update'),

    # Маршрут для удаления заказа
    # <int:pk> указывает на то, что это целочисленный параметр, представляющий первичный ключ заказа
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),

    # Маршрут для изменения статуса заказа
    # <int:pk> указывает на первичный ключ заказа, а <str:status> — на новый статус
    path('change-status/<int:pk>/<str:status>/', views.change_status, name='change_status'),

    # Маршрут для отображения выручки
    path('revenue/', views.revenue, name='revenue'),
]