from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import your custom registration view
from .views import register


urlpatterns = [
    # User registration
    path('register/', register, name='register'),
    
    # Login view (using Django's built-in view)
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

    # Logout view (using Django's built-in view)
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]
