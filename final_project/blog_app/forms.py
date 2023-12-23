from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django.forms import DateInput

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth', 'password1', 'password2']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['slug']