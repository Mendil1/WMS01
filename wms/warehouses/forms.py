from django import forms
from .models import Warehouse, InventoryMovement

class WarehouseForm(forms.ModelForm):
    """
    Form for creating and updating Warehouse instances.
    """
    class Meta:
        model = Warehouse
        fields = ['name', 'location']
        labels = {
            'name': 'Warehouse Name',
            'location': 'Location',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InventoryMovementForm(forms.ModelForm):
    """
    Form for creating and updating InventoryMovement instances.
    """
    class Meta:
        model = InventoryMovement
        fields = ['product', 'warehouse', 'quantity', 'movement_type', 'date_moved']
        labels = {
            'product': 'Product',
            'warehouse': 'Warehouse',
            'quantity': 'Quantity Moved',
            'movement_type': 'Movement Type',
            'date_moved': 'Date Moved',
        }
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'warehouse': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'movement_type': forms.Select(attrs={'class': 'form-control'}),
            'date_moved': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
