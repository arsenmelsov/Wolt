from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'phone_number', 'email', 'password',]

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']