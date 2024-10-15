from django.urls import path
from . import views
app_name = 'products'
urlpatterns =[
    path('', views.index, name='index'),
    # Category URLs
    path('categories/', views.category_list, name='category_list'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/update/<int:pk>/', views.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', views.category_delete, name='category_delete'),

    # Supplier URLs
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/update/<int:pk>/', views.supplier_update, name='supplier_update'),
    path('suppliers/delete/<int:pk>/', views.supplier_delete, name='supplier_delete'),

    # Product URLs
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/update/<int:pk>/', views.product_update, name='product_update'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
]


