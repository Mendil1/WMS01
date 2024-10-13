from django import forms
from .models import Order, OrderDetail, Shipment

# ----- ORDER FORM -----
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'order_status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'order_status': forms.Select(attrs={'class': 'form-control'}),
        }

# ----- ORDER DETAIL FORM -----
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['product', 'quantity_ordered', 'price_per_unit']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity_ordered': forms.NumberInput(attrs={'class': 'form-control'}),
            'price_per_unit': forms.NumberInput(attrs={'class': 'form-control'}),
        }

# ----- SHIPMENT FORM -----
class ShipmentForm(forms.ModelForm):
    # shipment_date = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly':'readonly'}), required=False)
    class Meta:
        model = Shipment
        fields = ['shipment_date', 'delivery_date', 'shipment_status', 'tracking_number']
        exclude = ['shipment_date']
        widgets = {
            'shipment_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'delivery_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'shipment_status': forms.Select(attrs={'class': 'form-control'}),
            'tracking_number': forms.TextInput(attrs={'class': 'form-control'}),
        }