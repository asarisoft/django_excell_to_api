from django import forms
from django.contrib import auth


class LoginForm(auth.forms.AuthenticationForm):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)

    def clean(self):
        return super(LoginForm, self).clean()
