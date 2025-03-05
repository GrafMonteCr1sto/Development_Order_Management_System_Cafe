from django.db import models

class Order(models.Model):
    """
    Модель Order представляет заказ в кафе.
    Она содержит информацию о номере стола, заказанных блюдах, общей стоимости и статусе заказа.
    """

    # Определение возможных статусов заказа
    STATUS_CHOICES = (
        ('waiting', 'В ожидании'),  # Заказ ожидает обработки
        ('ready', 'Готово'),        # Заказ готов к выдаче
        ('paid', 'Оплачено'),       # Заказ оплачен
    )

    # Номер стола, на который оформлен заказ
    table_number = models.PositiveIntegerField()

    # Список заказанных блюд с ценами, хранится в формате JSON
    # Пример: [{"name": "Пицца", "price": 150}]
    items = models.JSONField()

    # Общая стоимость заказа, вычисляется автоматически на основе списка блюд
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Статус заказа, по умолчанию "в ожидании"
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')

    def save(self, *args, **kwargs):
        """
        Переопределение метода save для автоматического расчета общей стоимости заказа
        на основе списка блюд перед сохранением в базу данных.
        """
        # Расчет общей стоимости заказа
        self.total_price = sum(item['price'] for item in self.items)

        # Вызов метода save родительского класса для сохранения объекта в базе данных
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Возвращает строковое представление объекта Order.
        Используется для отображения информации о заказе в административной панели Django.
        """
        return f"Заказ {self.id} на столе {self.table_number}"
