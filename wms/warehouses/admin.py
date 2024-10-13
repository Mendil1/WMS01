from django.contrib import admin
from .models import Warehouse, InventoryMovement

@admin.register(Warehouse)
class WarehouseAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('name', 'location')  # Shows warehouse name and location in admin list
    list_filter = ('location',)  # Add filter by location in the admin sidebar
    search_fields = ('name', 'location')  # Enable searching by name and location

    # Enable editing fields directly in the list view
    list_editable = ('location',)

    # Enable actions like delete, etc.
    actions = ['delete_selected']

    # Detail view: Organize fields in sections
    fieldsets = (
        (None, {
            'fields': ('name', 'location')
        }),
    )

@admin.register(InventoryMovement)
class InventoryMovementAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('product', 'warehouse', 'quantity', 'movement_type', 'date_moved')
    
    # Add filtering by movement type and date moved
    list_filter = ('movement_type', 'date_moved', 'warehouse')
    
    # Add search functionality by product and warehouse
    search_fields = ('product__name', 'warehouse__name')
    
    # Enable editing quantity and movement type directly in the list view
    list_editable = ('quantity', 'movement_type')

    # Display related fields in a detailed view
    fieldsets = (
        (None, {
            'fields': ('product', 'warehouse', 'quantity', 'movement_type', 'date_moved')
        }),
    )
    
    # Set ordering for list view
    ordering = ('-date_moved',)  # Orders by most recent movements

    # Enable actions like delete
    actions = ['delete_selected']
