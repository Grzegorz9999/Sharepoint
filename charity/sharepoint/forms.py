from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class CreateUserForm(UserCreationForm):
 #   class Meta:
  #      model = User
   #     fields = ['username', 'email', 'password1', 'password2']

class MyLoginForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)