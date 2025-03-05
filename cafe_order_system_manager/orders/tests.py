from django.test import TestCase
from django.urls import reverse
from .models import Order
from typing import Any, Dict, List

class OrderModelTest(TestCase):
    def setUp(self) -> None:
        """
        Создание тестового заказа перед каждым тестом.
        """
        self.order = Order.objects.create(
            table_number=1,
            items=[{"name": "Пицца", "price": 150}],
            status='waiting'
        )

    def test_total_price_calculation(self) -> None:
        """
        Проверка автоматического расчета общей стоимости заказа.
        """
        self.assertEqual(self.order.total_price, 150.00)

class OrderViewTest(TestCase):
    def setUp(self) -> None:
        """
        Создание тестового заказа перед каждым тестом.
        """
        self.order = Order.objects.create(
            table_number=1,
            items=[{"name": "Пицца", "price": 150}],
            status='waiting'
        )

    def test_order_list_view(self) -> None:
        """
        Проверка представления списка заказов.
        """
        response = self.client.get(reverse('order_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Список заказов")
        self.assertQuerysetEqual(response.context['orders'], [self.order])

    def test_order_create_view(self) -> None:
        """
        Проверка представления создания заказа.
        """
        response = self.client.post(reverse('order_create'), {
            'table_number': 2,
            'items': '[{"name": "Суп", "price": 100}]'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 2)

    def test_order_update_view(self) -> None:
        """
        Проверка представления обновления заказа.
        """
        response = self.client.post(reverse('order_update', args=(self.order.id,)), {
            'table_number': 2,
            'items': '[{"name": "Суп", "price": 100}]'
        })
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.table_number, 2)
        self.assertEqual(self.order.total_price, 100.00)

    def test_order_delete_view(self) -> None:
        """
        Проверка представления удаления заказа.
        """
        response = self.client.post(reverse('order_delete', args=(self.order.id,)))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 0)

    def test_change_status_view(self) -> None:
        """
        Проверка представления изменения статуса заказа.
        """
        response = self.client.get(reverse('change_status', args=(self.order.id, 'ready')))
        self.assertEqual(response.status_code, 302)
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'ready')

    def test_revenue_view(self) -> None:
        """
        Проверка представления расчета выручки.
        """
        # Создаем еще один оплаченный заказ
        Order.objects.create(
            table_number=2,
            items=[{"name": "Салат", "price": 75}],
            status='paid'
        )
        response = self.client.get(reverse('revenue'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Общая выручка")
        self.assertEqual(response.context['total_revenue'], 175.00)