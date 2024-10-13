from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm

# ----- CUSTOMER VIEWS -----

def customer_list(request):
    """List all customers."""
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_create(request):
    """Create a new customer."""
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm()
    return render(request, 'customers/customer_form.html', {'form': form})

def customer_update(request, pk):
    """Update an existing customer."""
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers:customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customers/customer_form.html', {'form': form})

def customer_delete(request, pk):
    """Delete a customer."""
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers:customer_list')
    return render(request, 'customers/customer_confirm_delete.html', {'customer': customer})

def customer_detail(request, pk):
    """View details of a specific customer."""
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers/customer_detail.html', {'customer': customer})
