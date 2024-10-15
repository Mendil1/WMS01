from django.urls import path
from . import views

app_name = 'warehouses'

urlpatterns = [
    # Index view
    path('', views.index, name='index'),

    # Warehouse views
    path('warehouses/', views.warehouse_list, name='warehouse_list'),
    path('warehouses/create/', views.warehouse_create, name='warehouse_create'),
    path('warehouses/<int:pk>/edit/', views.warehouse_update, name='warehouse_update'),
    path('warehouses/<int:pk>/delete/', views.warehouse_delete, name='warehouse_delete'),

    # Inventory Movement views
    path('movements/', views.movement_list, name='movement_list'),
    path('movements/create/', views.movement_create, name='movement_create'),
    path('movements/<int:pk>/edit/', views.movement_update, name='movement_update'),
    path('movements/<int:pk>/delete/', views.movement_delete, name='movement_delete'),
]
