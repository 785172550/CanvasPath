# coding:utf-8
# life is short, you need Python！
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'username', 'required': 'required',
                                          'autofocus': 'autofocus'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Password', 'required': 'required'}))
