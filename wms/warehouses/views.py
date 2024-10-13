from django.shortcuts import render, get_object_or_404, redirect
from .models import Warehouse, InventoryMovement
from .forms import WarehouseForm, InventoryMovementForm

def index(request):
    """View function for the home page of the Warehouses App."""
    warehouses = Warehouse.objects.all()  # Get all warehouses
    movements = InventoryMovement.objects.all()  # Get all inventory movements

    context = {
        'warehouses': warehouses,
        'movements': movements,
    }
    return render(request, 'warehouses/index.html', context)


# ----- WAREHOUSE VIEWS -----

def warehouse_list(request):
    """List all warehouses."""
    warehouses = Warehouse.objects.all()
    return render(request, 'warehouses/warehouse_list.html', {'warehouses': warehouses})


def warehouse_create(request):
    """Create a new warehouse."""
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouses:warehouse_list')
    else:
        form = WarehouseForm()
    return render(request, 'warehouses/warehouse_form.html', {'form': form})


def warehouse_update(request, pk):
    """Update an existing warehouse."""
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        form = WarehouseForm(request.POST, instance=warehouse)
        if form.is_valid():
            form.save()
            return redirect('warehouses:warehouse_list')
    else:
        form = WarehouseForm(instance=warehouse)
    return render(request, 'warehouses/warehouse_form.html', {'form': form})


def warehouse_delete(request, pk):
    """Delete a warehouse."""
    warehouse = get_object_or_404(Warehouse, pk=pk)
    if request.method == 'POST':
        warehouse.delete()
        return redirect('warehouses:warehouse_list')
    return render(request, 'warehouses/warehouse_confirm_delete.html', {'warehouse': warehouse})


# ----- INVENTORY MOVEMENT VIEWS -----

def movement_list(request):
    """List all inventory movements."""
    movements = InventoryMovement.objects.all()
    return render(request, 'warehouses/movement_list.html', {'movements': movements})


def movement_create(request):
    """Create a new inventory movement."""
    if request.method == 'POST':
        form = InventoryMovementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouses:movement_list')
    else:
        form = InventoryMovementForm()
    return render(request, 'warehouses/movement_form.html', {'form': form})


def movement_update(request, pk):
    """Update an existing inventory movement."""
    movement = get_object_or_404(InventoryMovement, pk=pk)
    if request.method == 'POST':
        form = InventoryMovementForm(request.POST, instance=movement)
        if form.is_valid():
            form.save()
            return redirect('warehouses:movement_list')
    else:
        form = InventoryMovementForm(instance=movement)
    return render(request, 'warehouses/movement_form.html', {'form': form})


def movement_delete(request, pk):
    """Delete an inventory movement."""
    movement = get_object_or_404(InventoryMovement, pk=pk)
    if request.method == 'POST':
        movement.delete()
        return redirect('warehouses:movement_list')
    return render(request, 'warehouses/movement_confirm_delete.html', {'movement': movement})
