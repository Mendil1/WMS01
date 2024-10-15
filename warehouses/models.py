from django.db import models
from django.utils import timezone
from products.models import Product  # Assuming Product model is in products app

class Warehouse(models.Model):
    """
    Model to represent a Warehouse
    """
    name = models.CharField(max_length=255, unique=True, verbose_name="Warehouse Name")
    location = models.CharField(max_length=255, verbose_name="Location")

    def __str__(self):
        return f"{self.name} ({self.location})"

    def get_total_stock(self, product):
        """
        Returns the total stock of a given product in this warehouse
        """
        stock_in = self.inventory_movements.filter(product=product, movement_type='IN').aggregate(total_in=models.Sum('quantity'))['total_in'] or 0
        stock_out = self.inventory_movements.filter(product=product, movement_type='OUT').aggregate(total_out=models.Sum('quantity'))['total_out'] or 0
        return stock_in - stock_out

    class Meta:
        verbose_name = "Warehouse"
        verbose_name_plural = "Warehouses"
        ordering = ['name']


class InventoryMovement(models.Model):
    """
    Model to track product inventory movements (in and out of warehouses)
    """
    MOVEMENT_TYPES = (
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out')
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inventory_movements', verbose_name="Product")
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='inventory_movements', verbose_name="Warehouse")
    quantity = models.PositiveIntegerField(verbose_name="Quantity Moved")
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES, verbose_name="Movement Type")
    date_moved = models.DateTimeField(default=timezone.now, verbose_name="Date Moved")

    def save(self, *args, **kwargs):
        """
        Override the save method to handle stock validation before creating movement records
        """
        if self.movement_type == 'OUT' and not self.is_stock_sufficient():
            raise ValueError(f"Not enough stock of {self.product.product_name} in warehouse {self.warehouse.name} to complete the movement.")
        super().save(*args, **kwargs)

    def is_stock_sufficient(self):
        """
        Check if there is enough stock in the warehouse before an OUT movement
        """
        current_stock = self.warehouse.get_total_stock(self.product)
        return current_stock >= self.quantity

    def __str__(self):
        return f"{self.movement_type} {self.quantity} of {self.product.product_name} at {self.warehouse.name} on {self.date_moved.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Inventory Movement"
        verbose_name_plural = "Inventory Movements"
        ordering = ['-date_moved']
