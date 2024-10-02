# forms.py

from django import forms
from .models import Startup

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
