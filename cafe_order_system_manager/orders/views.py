from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

# Отображение списка всех заказов
def order_list(request):
    # Получаем все заказы из базы данных
    orders = Order.objects.all()

    # Получаем параметр поиска из GET-запроса
    query = request.GET.get('q')

    # Фильтруем заказы по номеру стола или статусу, если указан параметр поиска
    if query:
        orders = orders.filter(table_number=query) | orders.filter(status__icontains=query)

    # Рендерим шаблон с отфильтрованным списком заказов
    return render(request, 'orders/order_list.html', {'orders': orders})

# Создание нового заказа
def order_create(request):
    if request.method == 'POST':
        # Обрабатываем POST-запрос с данными нового заказа
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        # Отображаем пустую форму для создания нового заказа
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

# Обновление существующего заказа
def order_update(request, pk):
    # Получаем заказ по первичному ключу или возвращаем 404 ошибку, если заказ не найден
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        # Обрабатываем POST-запрос с обновленными данными заказа
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        # Отображаем форму с текущими данными заказа
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

# Удаление заказа
def order_delete(request, pk):
    # Получаем заказ по первичному ключу или возвращаем 404 ошибку, если заказ не найден
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'POST':
        # Удаляем заказ из базы данных
        order.delete()
        return redirect('order_list')

    # Отображаем страницу подтверждения удаления
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

# Изменение статуса заказа
def change_status(request, pk, status):
    # Получаем заказ по первичному ключу или возвращаем 404 ошибку, если заказ не найден
    order = get_object_or_404(Order, pk=pk)

    # Проверяем, что новый статус является допустимым
    if status in [choice[0] for choice in Order.STATUS_CHOICES]:
        order.status = status
        order.save()

    # Перенаправляем на страницу со списком заказов
    return redirect('order_list')

# Отображение общей выручки
def revenue(request):
    # Получаем все оплаченные заказы
    paid_orders = Order.objects.filter(status='paid')

    # Рассчитываем общую выручку как сумму стоимостей всех оплаченных заказов
    total_revenue = sum(order.total_price for order in paid_orders)

    # Рендерим шаблон с общей выручкой
    return render(request, 'orders/revenue.html', {'total_revenue': total_revenue})