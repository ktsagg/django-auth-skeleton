# accounts.forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Extends the django.contrib.auth.forms.AuthenticationForm
    to provide a custom label fro username field.
    """
    username = forms.CharField(max_length=254, label='Username/Email')


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email',)
        """
        labels = {
            'first_name': 'Ονομα',
            'last_name': 'Επώνυμο',
            'username': 'Ονομα Εισόδου',
            'password1': 'Κωδικός Εισόδου',
            'password2': 'Επιβεβαίωση Κωδικού Εισόδου'
        }
        """
