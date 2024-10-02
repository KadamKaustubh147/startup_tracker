# forms.py

from django import forms
from .models import Startup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# KYC Form using ModelForm
class StartupKYCForm(forms.ModelForm):
    class Meta:
        model = Startup  # Link the form to the Startup model
        fields = ['name', 'address', 'contact', 'company_details']  # Fields to be displayed in the form
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Startup Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number or Email'}),
            'company_details': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your company'}),
        }

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Adding an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Specify the fields to include
