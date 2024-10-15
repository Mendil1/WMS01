from django.db import models
from customers.models import Customer  # Assuming Customer is in the customers app
from products.models import Product    # Assuming Product is in the products app

# ----- ORDER MODEL -----
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Completed', 'Completed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id} - {self.customer.name}"

    def calculate_total(self):
        """Calculate the total amount based on the order details."""
        total = sum(detail.total_price for detail in self.orderdetail_set.all())
        self.total_amount = total
        self.save()

# ----- ORDER DETAIL MODEL -----
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def __str__(self):
        return f"{self.product.product_name} - {self.quantity_ordered} units"

    def save(self, *args, **kwargs):
        """Override save to calculate the total price."""
        self.total_price = self.quantity_ordered * self.price_per_unit
        super().save(*args, **kwargs)
        # Recalculate the order total amount after saving the detail
        self.order.calculate_total()

# ----- SHIPMENT MODEL -----
class Shipment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Transit', 'In Transit'),
        ('Delivered', 'Delivered'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    shipment_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    shipment_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    tracking_number = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Shipment #{self.id} - {self.order}"

    def is_delivered(self):
        """Check if the shipment is delivered."""
        return self.shipment_status == 'Delivered'
