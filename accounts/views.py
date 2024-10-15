from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from customers.models import Customer  # Import the Customer model


def test_view(request):
    return render(request, 'accounts/test.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            phone_number = form.cleaned_data.get('phone_number')

            # Save the phone number in the customers_customer table
            Customer.objects.create(
                name=user.username,  # Or you can collect the full name separately
                phone_number=phone_number,
                email=user.email,
                address="N/A"  # You can collect this too, or leave it as default for now
            )

            login(request, user)  # Automatically log in the user
            return redirect('home')  # Redirect to home page after registration
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})
