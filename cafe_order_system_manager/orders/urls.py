from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('update/<int:pk>/', views.order_update, name='order_update'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('change-status/<int:pk>/<str:status>/', views.change_status, name='change_status'),
    path('revenue/', views.revenue, name='revenue'),
]