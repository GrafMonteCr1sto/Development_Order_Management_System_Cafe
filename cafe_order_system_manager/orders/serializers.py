from rest_framework import serializers
from .models import Order

# Определение сериализатора для модели Order
class OrderSerializer(serializers.ModelSerializer):
    # Вложенный класс Meta содержит метаданные для сериализатора
    class Meta:
        # Указываем модель, с которой связан этот сериализатор
        model = Order

        # Указываем, что все поля модели должны быть сериализованы
        fields = '__all__'