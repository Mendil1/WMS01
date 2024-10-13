from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name
    
    def get_product_count(self):
        """Return the number of products in this category."""
        return self.product_set.count()  # Assuming related name is default

class Supplier(models.Model):
    supplier_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.supplier_name
    
    def get_full_contact_info(self):
        """Return a formatted string with full contact information."""
        return f"{self.supplier_name}, Phone: {self.phone_number}, Email: {self.email}, Address: {self.address}"

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    quantity_in_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.product_name

    def total_value(self):
        """Calculate the total value of stock for this product."""
        return self.quantity_in_stock * self.price_per_unit

    def needs_reorder(self):
        """Check if the product needs to be reordered."""
        return self.quantity_in_stock <= self.reorder_level

    def is_in_stock(self):
        """Check if the product is currently in stock."""
        return self.quantity_in_stock > 0

    def update_stock(self, quantity):
        """Update stock quantity; """
        self.quantity_in_stock += quantity
        self.save()