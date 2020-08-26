from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "form-control"}))
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))