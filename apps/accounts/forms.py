# accounts.forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


###############################################################################
class LoginForm(AuthenticationForm):
    """
    Extends the django.contrib.auth.forms.AuthenticationForm
    to provide a custom label fro username field.
    """
    username = forms.CharField(max_length=254, label='Username/Email')


###############################################################################
class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)

