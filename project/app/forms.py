from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import MyUser


class RegisetrForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']


class SignInForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password')
