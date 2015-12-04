# From Django Module Imports:
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login, authenticate, get_user
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib.auth.models import User

# From Third Party Package Imports:
import json

# From Current Project Module Imports:
from userprofile.forms import UserLoginForm, UserRegisterForm

class UserLoginView(FormView):

    template_name = "user_login.html"
    success_url = "/"
    form_class = UserLoginForm
    user_error = "username or password incorrect."

    def form_valid(self, form):
        user = authenticate(username=self.request.POST.get('username'), \
                            password = self.request.POST.get('password'))
        if user is not None:
            auth_login(self.request, user)
            return super(UserLoginView, self).form_valid(form)
        return render(self.request, self.template_name, {
            'form':form, 'user_error':self.user_error
        })

class UserRegistrationView(FormView):

    template_name = "user_register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        User.objects.create_user(username = self.request.POST.get('username'), \
            email = self.request.POST.get('email'), password = self.request.POST.get('password'))
        return super(UserRegistrationView, self).form_valid(form)

class HomePage(TemplateView):

    template_name = 'index.html'

class HospitalsListView(TemplateView):

    template_name = 'hospitals.html'

class ClinicsPageView(TemplateView):

    template_name = 'clinics.html'

class DgLabsPageView(TemplateView):

    template_name = 'dglabs.html'

class PharmacyPageview(TemplateView):

    template_name = 'pharmacy.html'

class ContactPageView(TemplateView):

    template_name = 'contact.html'

class HospitalPageView(TemplateView):

    template_name = 'hospital.html'
