from django import forms
from django.forms import ModelForm


class UserLoginForm(forms.Form):

    username = forms.CharField(label = ("Username"), max_length = 20, \
                widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label = ("Password"), \
                widget = forms.PasswordInput(attrs = {'class':'form-control'}))
