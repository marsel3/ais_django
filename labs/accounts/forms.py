from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'placeholder': 'Имя пользователя'}),
        max_length=150,
        required=True
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
        strip=False,
        required=True
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
        strip=False,
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
