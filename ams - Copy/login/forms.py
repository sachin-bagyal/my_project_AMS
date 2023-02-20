from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=12, min_length=4, required=True, help_text='Required: Username',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(max_length=40, min_length=5, required=True, help_text='Required: Username',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(max_length=10, min_length=4, required=True, help_text='Required: Username',
                                widget=forms.TextInput(attrs={'type' :'password','class': 'form-control', 'placeholder': 'Username'}))
    password2 = forms.CharField(max_length=10, min_length=4, required=True, help_text='Required: Username',
                                widget=forms.TextInput(attrs={'type': 'password','class': 'form-control', 'placeholder': 'Username'}))

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
