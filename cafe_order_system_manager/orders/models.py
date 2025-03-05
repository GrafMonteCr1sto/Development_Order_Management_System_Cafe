from django.db import models

# Определение модели Order
class Order(models.Model):
    # Определение возможных статусов заказа
    STATUS_CHOICES = (
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    )

    # Номер стола, положительное целое число
    table_number = models.PositiveIntegerField()

    # Список заказанных блюд с ценами, хранится в формате JSON
    items = models.JSONField()  # Пример: [{"name": "Пицца", "price": 150}]

    # Общая стоимость заказа, вычисляется автоматически
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Статус заказа, выбирается из предопределенных значений
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')

    # Переопределение метода save для автоматического расчета общей стоимости заказа
    def save(self, *args, **kwargs):
        # Рассчитываем общую стоимость как сумму цен всех блюд
        self.total_price = sum(item['price'] for item in self.items)
        # Вызываем метод save родительского класса
        super().save(*args, **kwargs)

    # Возвращает строковое представление заказа
    def __str__(self):
        return f"Заказ {self.id} на столе {self.table_number}"