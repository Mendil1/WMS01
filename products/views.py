from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Category, Supplier, Product
from .forms import ProductForm, CategoryForm, SupplierForm
def index(request):
    """View function for the home page of the Products App."""
    
    # Optionally retrieve data you want to display
    categories = Category.objects.all()  # Get all categories
    suppliers = Supplier.objects.all()  # Get all suppliers
    products = Product.objects.all()  # Get all products

    context = {
        'categories': categories,
        'suppliers': suppliers,
        'products': products,
    }
    
    return render(request, 'products/index.html', context)

def category_list(request):
    """List all categories."""
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})


def category_create(request):
    """Create a new category."""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')
    else:
        form = CategoryForm()
    return render(request, 'products/category_form.html', {'form': form})
def category_update(request, pk):
    """Update an existing category."""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('products:category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'products/category_form.html', {'form': form})

def category_delete(request, pk):
    """Delete a category."""
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('products:category_list')
    return render(request, 'products/category_confirm_delete.html', {'category': category})

# ----- SUPPLIER VIEWS -----

def supplier_list(request):
    """List all suppliers."""
    suppliers = Supplier.objects.all()
    return render(request, 'products/supplier_list.html', {'suppliers': suppliers})

def supplier_create(request):
    """Create a new supplier."""
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'products/supplier_form.html', {'form': form})

def supplier_update(request, pk):
    """Update an existing supplier."""
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('products:supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'products/supplier_form.html', {'form': form})

def supplier_delete(request, pk):
    """Delete a supplier."""
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('products:supplier_list')
    return render(request, 'products/supplier_confirm_delete.html', {'supplier': supplier})

# ----- PRODUCT VIEWS -----

def product_list(request):
    """List all products."""
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, pk):
    """Show the details of a specific product."""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

def product_create(request):
    """Create a new product."""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_form.html', {'form': form})

def product_update(request, pk):
    """Update an existing product."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form})

def product_delete(request, pk):
    """Delete a product."""
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products:product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})