from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и @/./+/-/_'
    )
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Пароль должен содержать минимум 8 символов'
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text='Повторите пароль для проверки'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'steps': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'cooking_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }