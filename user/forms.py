from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from user.models import User


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control py-4",
    'placeholder':"Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control py-4",
    'placeholder':'Введите пароль'}))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control py-4",
    'placeholder':"Имя"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':"form-control py-4",
    'placeholder':'Фамилия'}))
    username =  forms.CharField(widget=forms.TextInput(attrs={'class':"form-control py-4",
    'placeholder':'Логин для быстрого входа'}))
    email =  forms.CharField(widget=forms.EmailInput(attrs={'class':"form-control py-4",
    'placeholder':"Адрес электронной почты"}))
    password1 =  forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control py-4",
    'placeholder':"Введите пароль"}))
    password2 =  forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control py-4",
    'placeholder':"Повторите пароль"}))
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1','password2')
