from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    """
    Отображение списка заказов с возможностью поиска по номеру стола или статусу.
    """
    query = request.GET.get('q')
    if query:
        try:
            # Поиск по номеру стола
            table_number = int(query)
            orders = Order.objects.filter(table_number=table_number)
        except ValueError:
            # Поиск по статусу, если ввод не является числом
            orders = Order.objects.filter(status__icontains=query)
        return render(request, 'orders/order_search_results.html', {'orders': orders, 'query': query})
    else:
        # Отображение всех заказов, если поисковый запрос отсутствует
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    """
    Создание нового заказа.
    """
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_update(request, pk):
    """
    Обновление существующего заказа.
    """
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, pk):
    """
    Удаление заказа.
    """
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

def change_status(request, pk, status):
    """
    Изменение статуса заказа.
    """
    order = get_object_or_404(Order, pk=pk)
    if status in [choice[0] for choice in Order.STATUS_CHOICES]:
        order.status = status
        order.save()
    return redirect('order_list')

def revenue(request):
    """
    Расчет общей выручки за смену на основе оплаченных заказов.
    """
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = sum(order.total_price for order in paid_orders)
    return render(request, 'orders/revenue.html', {'total_revenue': total_revenue})