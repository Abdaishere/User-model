from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class createAccount(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password1','password2', 'is_staff']

class changeAccount(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password']

