from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    # ----- ORDER URLS -----
    path('', views.order_list, name='order_list'),
    path('create/', views.order_create, name='order_create'),
    path('<int:pk>/', views.order_detail, name='order_detail'),
    path('<int:pk>/edit/', views.order_update, name='order_update'),
    path('<int:pk>/delete/', views.order_delete, name='order_delete'),

    # ----- ORDER DETAIL URLS -----
    path('<int:order_id>/details/add/', views.order_detail_create, name='order_detail_create'),
    path('<int:order_id>/details/<int:detail_id>/edit/', views.order_detail_update, name='order_detail_update'),
    path('<int:order_id>/details/<int:detail_id>/delete/', views.order_detail_delete, name='order_detail_delete'),

    # ----- SHIPMENT URLS -----
    path('<int:order_id>/shipment/', views.shipment_detail, name='shipment_detail'),
    path('<int:order_id>/shipment/create/', views.shipment_create, name='shipment_create'), 
    path('shipment/<int:pk>/edit/', views.shipment_update, name='shipment_update'),
    # path('<int:order_id>/shipment/edit/', views.shipment_update, name='shipment_update'),
    path('shipments/', views.shipment_list, name='shipment_list'),
    path('<int:pk>/shipment/delete/', views.shipment_delete, name='shipment_delete'),
]
