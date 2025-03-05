from django.test import TestCase
from django.urls import reverse
from .models import Order

# Тесты для модели Order
class OrderModelTest(TestCase):
    # Метод setUp выполняется перед каждым тестом для подготовки данных
    def setUp(self):
        self.order = Order.objects.create(
            table_number=1,
            items=[{"name": "Пицца", "price": 150}],
            status='waiting'
        )

    # Тест для проверки корректности расчета общей стоимости заказа
    def test_total_price_calculation(self):
        self.assertEqual(self.order.total_price, 150.00)

# Тесты для представлений, связанных с заказами
class OrderViewTest(TestCase):
    # Метод setUp выполняется перед каждым тестом для подготовки данных
    def setUp(self):
        self.order = Order.objects.create(
            table_number=1,
            items=[{"name": "Пицца", "price": 150}],
            status='waiting'
        )

    # Тест для проверки отображения списка заказов
    def test_order_list_view(self):
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Список заказов")
        self.assertQuerysetEqual(response.context['orders'], [self.order])

    # Тест для проверки создания нового заказа
    def test_order_create_view(self):
        response = self.client.post(reverse('order_create'), {
            'table_number': 2,
            'items': '[{"name": "Суп", "price": 100}]'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 2)

    # Тест для проверки обновления существующего заказа
    def test_order_update_view(self):
        response = self.client.post(reverse('order_update', args=(self.order.id,)), {
            'table_number': 2,
            'items': '[{"name": "Суп", "price": 100}]'
        })
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.table_number, 2)
        self.assertEqual(self.order.total_price, 100.00)

    # Тест для проверки удаления заказа
    def test_order_delete_view(self):
        response = self.client.post(reverse('order_delete', args=(self.order.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 0)

    # Тест для проверки изменения статуса заказа
    def test_change_status_view(self):
        response = self.client.get(reverse('change_status', args=(self.order.id, 'ready')))
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'ready')

    # Тест для проверки отображения выручки
    def test_revenue_view(self):
        response = self.client.get(reverse('revenue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Общая выручка")