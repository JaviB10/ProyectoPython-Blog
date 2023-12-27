from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import DateInput
from .models import *

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(UserCreationForm):
    # Campo adicional para la fecha de nacimiento
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
    # Campo adicional para eliminar la imagen
    clear = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    class Meta:
        model = Avatar
        fields = ['image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'categories', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'message']

    def __init__(self, *args, **kwargs):
        # Filtra la lista de usuarios para excluir al remitente actual
        sender = kwargs.pop('sender', None)
        super(MessageForm, self).__init__(*args, **kwargs)
        if sender:
            self.fields['receiver'].queryset = User.objects.exclude(username=sender.username)