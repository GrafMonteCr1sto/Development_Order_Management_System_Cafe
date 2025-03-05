from django.urls import path
from . import views

# Список маршрутов URL для приложения
urlpatterns = [
    # Основная страница, отображающая список всех заказов
    path('', views.order_list, name='order_list'),

    # Страница для создания нового заказа
    path('create/', views.order_create, name='order_create'),

    # Страница для обновления существующего заказа по его ID (pk)
    path('update/<int:pk>/', views.order_update, name='order_update'),

    # Страница для удаления заказа по его ID (pk)
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),

    # Страница для изменения статуса заказа по его ID (pk) и новому статусу
    path('change-status/<int:pk>/<str:status>/', views.change_status, name='change_status'),

    # Страница для расчета выручки за смену
    path('revenue/', views.revenue, name='revenue'),
]