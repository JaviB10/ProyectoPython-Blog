from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.forms import UserChangeForm
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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['description', 'website']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date_of_birth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AvatarForm(forms.ModelForm):
    clear = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    class Meta:
        model = Avatar
        fields = ['image']  # Reemplaza 'image' con el campo real que almacena la imagen del avatar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el formulario según tus necesidades

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'categories', 'is_published', 'image']  # Reemplaza 'image' con el campo real que almacena la imagen del avatar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el formulario según tus necesidades

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Reemplaza 'image' con el campo real que almacena la imagen del avatar

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza el formulario según tus necesidades

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'message']  # Reemplaza 'image' con el campo real que almacena la imagen del avatar

    def __init__(self, *args, **kwargs):
        # Filtra la lista de usuarios para excluir al remitente actual
        sender = kwargs.pop('sender', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if sender:
            self.fields['receiver'].queryset = User.objects.exclude(username=sender.username)