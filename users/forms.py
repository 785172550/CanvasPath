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


class CourseForm(forms.Form):
    course_id = forms.CharField(label="course id",
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'course id', 'required': 'required',
                                           'autofocus': 'autofocus'}))
    course_name = forms.CharField(label="course_name",
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': 'name', 'required': 'required'}))
    course_description = forms.CharField(label="course_description",
                                         widget=forms.TextInput(
                                             attrs={'class': 'form-control', 'placeholder': 'description'}))


class UserForm(forms.Form):
    username = forms.CharField(label="username",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'course id', 'required': 'required',
                                          'autofocus': 'autofocus'}))
    email = forms.CharField(label="email",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'name', 'required': 'required'}))
    password = forms.CharField(label="password",
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'description',
                                          'required': 'required'}))
    role = forms.CharField(label="role",
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'description', 'required': 'required'}))

    name = forms.CharField(label="name",
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'description'}))

