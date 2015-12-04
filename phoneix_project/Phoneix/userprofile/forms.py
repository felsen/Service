# From Dajngo Package Imports:
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):

    username = forms.CharField(label = ("Username"), max_length = 20, \
                widget = forms.TextInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label = ("Password"), \
                widget = forms.PasswordInput(attrs = {'class':'form-control'}))

class UserRegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(label = ("Confirm Password"), \
                widget = forms.PasswordInput(attrs = {'class':'form-control'}), required = True)
    email = forms.EmailField(label = "Email Address", \
                widget = forms.EmailInput(attrs = {'class':'form-control'}), required = True)

    class Meta:
        model = User
        fields = ("username", "password", "confirm_password", "email")
        widgets = {"username":forms.TextInput(attrs = {'class':'form-control'}),
                   "password":forms.PasswordInput(attrs = {'class':'form-control'}),}

    def clean_confirm_password(self):
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['confirm_password']
        if pwd1 != pwd2:
            raise forms.ValidationError("password and confirm password should be match.")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError("Email already exists.")
        return email





