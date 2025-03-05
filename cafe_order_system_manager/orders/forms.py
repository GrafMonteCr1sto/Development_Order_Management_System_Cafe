from django import forms
from .models import Order

# Определение формы для модели Order
class OrderForm(forms.ModelForm):
    # Вложенный класс Meta содержит метаданные для формы
    class Meta:
        # Указываем модель, с которой связана эта форма
        model = Order

        # Список полей модели, которые будут включены в форму
        fields = ['table_number', 'items']