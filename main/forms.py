from django.forms import ModelForm
from django.shortcuts import redirect
from main.models import User, MyUser
from django.contrib.auth.forms import UserCreationForm, forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class PictureForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['image', 'user']

