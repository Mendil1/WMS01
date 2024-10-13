from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderDetail, Shipment
from .forms import OrderForm, OrderDetailForm, ShipmentForm

# ----- ORDER VIEWS -----

def order_list(request):
    """List all orders."""
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_create(request):
    """Create a new order."""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

def order_detail(request, pk):
    """Show details of a specific order including order details and shipment status."""
    order = get_object_or_404(Order, pk=pk)
    order_details = OrderDetail.objects.filter(order=order)
    shipment = Shipment.objects.filter(order=order).first()
    return render(request, 'orders/order_detail.html', {
        'order': order, 
        'order_details': order_details,
        'shipment': shipment
    })

def order_update(request, pk):
    """Update an existing order."""
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

def order_delete(request, pk):
    """Delete an order."""
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('orders:order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})

# ----- ORDER DETAIL VIEWS -----

def order_detail_create(request, order_id):
    """Create a new order detail (for a specific order)."""
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderDetailForm(request.POST)
        if form.is_valid():
            order_detail = form.save(commit=False)
            order_detail.order = order
            order_detail.save()
            return redirect('orders:order_detail', pk=order.id)
    else:
        form = OrderDetailForm()
    return render(request, 'orders/order_detail_form.html', {'form': form, 'order': order})

def order_detail_update(request, pk):
    """Update an existing order detail."""
    order_detail = get_object_or_404(OrderDetail, pk=pk)
    if request.method == 'POST':
        form = OrderDetailForm(request.POST, instance=order_detail)
        if form.is_valid():
            form.save()
            return redirect('orders:order_detail', pk=order_detail.order.id)
    else:
        form = OrderDetailForm(instance=order_detail)
    return render(request, 'orders/order_detail_form.html', {'form': form})

def order_detail_delete(request, pk):
    """Delete an order detail."""
    order_detail = get_object_or_404(OrderDetail, pk=pk)
    if request.method == 'POST':
        order_id = order_detail.order.id
        order_detail.delete()
        return redirect('orders:order_detail', pk=order_id)
    return render(request, 'orders/order_detail_confirm_delete.html', {'order_detail': order_detail})

# ----- SHIPMENT VIEWS -----

def shipment_create(request, order_id):
    """Create a new shipment for an order."""
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.order = order
            shipment.save()
            return redirect('orders:order_detail', pk=order.id)
    else:
        form = ShipmentForm()
    return render(request, 'orders/shipment_form.html', {'form': form, 'order': order})

def shipment_update(request, pk):
    """Update an existing shipment."""
    shipment = get_object_or_404(Shipment, pk=pk)
    if request.method == 'POST':
        form = ShipmentForm(request.POST, instance=shipment)
        if form.is_valid():
            form.save()
            return redirect('orders:order_detail', pk=shipment.order.id)
    else:
        form = ShipmentForm(instance=shipment)
    return render(request, 'orders/shipment_form.html', {'form': form})

def shipment_delete(request, pk):
    """Delete a shipment."""
    shipment = get_object_or_404(Shipment, pk=pk)
    if request.method == 'POST':
        order_id = shipment.order.id
        shipment.delete()
        return redirect('orders:order_detail', pk=order_id)
    return render(request, 'orders/shipment_confirm_delete.html', {'shipment': shipment})

def shipment_list(request):
    """List all shipments."""
    shipments = Shipment.objects.all()
    return render(request, 'orders/shipment_list.html', {'shipments': shipments})

def shipment_detail(request, order_id):
    """View details of a shipment for a specific order."""
    shipment = get_object_or_404(Shipment, order__id=order_id)
    return render(request, 'orders/shipment_detail.html', {'shipment': shipment})
