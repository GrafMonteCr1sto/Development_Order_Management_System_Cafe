from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from .forms import OrderForm

def order_list(request):
    query = request.GET.get('q')
    if query:
        try:
            table_number = int(query)
            orders = Order.objects.filter(table_number=table_number)
        except ValueError:
            orders = Order.objects.filter(status__icontains=query)
        return render(request, 'orders/order_search_results.html', {'orders': orders, 'query': query})
    else:
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_update(request, pk):
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
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

def change_status(request, pk, status):
    order = get_object_or_404(Order, pk=pk)
    if status in [choice[0] for choice in Order.STATUS_CHOICES]:
        order.status = status
        order.save()
    return redirect('order_list')

def revenue(request):
    paid_orders = Order.objects.filter(status='paid')
    total_revenue = sum(order.total_price for order in paid_orders)
    return render(request, 'orders/revenue.html', {'total_revenue': total_revenue})