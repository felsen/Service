from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def registration(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = User.objects.create_user(username = username, email = email, password = password)
    return HttpResponseRedirect('/')


def login(request):

    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('auth_password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
    return HttpResponseRedirect('/')

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
