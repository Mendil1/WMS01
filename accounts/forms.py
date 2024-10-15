from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from customers.models import Customer  # Import the Customer model

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)  # New field for phone number

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
