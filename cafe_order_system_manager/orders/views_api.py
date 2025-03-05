from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer

# Определение ViewSet для модели Order
class OrderViewSet(viewsets.ModelViewSet):
    # Указываем, какие объекты будут обрабатываться этим ViewSet
    queryset = Order.objects.all()

    # Указываем сериализатор, который будет использоваться для преобразования объектов в JSON и обратно
    serializer_class = OrderSerializer