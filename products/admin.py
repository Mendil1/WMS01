from django.contrib import admin
from .models import Category, Supplier, Product

# Inline for OrderDetails
class ProductInline(admin.TabularInline):
    model = Product
    extra = 0  # Number of empty forms to display

# Category Admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'get_product_count')  # Show category name and product count
    search_fields = ('category_name',)
    inlines = [ProductInline]  # Show products under category

    def get_product_count(self, obj):
        return obj.get_product_count()
    get_product_count.short_description = 'Number of Products'

# Supplier Admin
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_name', 'phone_number', 'email', 'address', 'product_count')
    search_fields = ('supplier_name',)
    ordering = ('supplier_name',)

    def product_count(self, obj):
        return obj.product_count()
    product_count.short_description = 'Number of Products'

# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category', 'supplier', 'quantity_in_stock', 'reorder_level', 'price_per_unit', 'total_value', 'needs_reorder')
    search_fields = ('product_name', 'supplier__supplier_name', 'category__category_name')
    list_filter = ('category', 'supplier')
    ordering = ('product_name',)

    def needs_reorder(self, obj):
        return obj.needs_reorder()
    needs_reorder.boolean = True  # Display as a boolean icon
    needs_reorder.short_description = 'Needs Reorder'

    def total_value(self, obj):
        return obj.total_value()
    total_value.short_description = 'Total Value'

# Register models with the admin site
admin.site.register(Category, CategoryAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Product, ProductAdmin)
