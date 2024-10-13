from django.contrib import admin
from .models import Order, OrderDetail, Shipment

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail
    extra = 1
    readonly_fields = ['total_price']

class ShipmentInline(admin.StackedInline):
    model = Shipment
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order_date', 'order_status', 'total_amount']
    list_filter = ['order_status', 'order_date']
    search_fields = ['customer__name', 'id']
    inlines = [OrderDetailInline, ShipmentInline]

    def save_model(self, request, obj, form, change):
        """Recalculate the total amount before saving the order."""
        obj.calculate_total()
        super().save_model(request, obj, form, change)

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity_ordered', 'price_per_unit', 'total_price']
    list_filter = ['order', 'product']
    search_fields = ['order__id', 'product__product_name']
    readonly_fields = ['total_price']

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'shipment_date', 'delivery_date', 'shipment_status', 'tracking_number']
    list_filter = ['shipment_status', 'shipment_date', 'delivery_date']
    search_fields = ['order__id', 'tracking_number']
