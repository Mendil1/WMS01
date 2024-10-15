from django.db import models

class Customer(models.Model):
    """Model representing a customer."""
    name = models.CharField(max_length=255, verbose_name="Customer Name")
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    email = models.EmailField(unique=True, verbose_name="Email")
    address = models.TextField(verbose_name="Address")

    def __str__(self):
        return self.name
