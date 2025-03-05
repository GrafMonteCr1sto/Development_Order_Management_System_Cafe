from django.db import models

class Order(models.Model):
    STATUS_CHOICES = (
        ('waiting', 'В ожидании'),
        ('ready', 'Готово'),
        ('paid', 'Оплачено'),
    )

    table_number = models.PositiveIntegerField()
    items = models.JSONField()  # Пример: [{"name": "Пицца", "price": 150}]
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='waiting')

    def save(self, *args, **kwargs):
        self.total_price = sum(item['price'] for item in self.items)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Заказ {self.id} на столе {self.table_number}"