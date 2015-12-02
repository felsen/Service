# From Django Module Imports:
from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.contrib.auth import login as auth_login, authenticate, get_user
from django.http import HttpResponseRedirect
from django.views.generic import FormView, View
from django.contrib.auth.models import User

# From Current Project Module Imports:
from userprofile.forms import UserLoginForm

class UserLoginView(FormView):

    template_name = "user_login.html"
    success_url = "/"
    form_class = UserLoginForm
    user_error = "username or password incorrect."

    def form_valid(self, form):
        user = authenticate(username = self.request.POST.get('username'), password = self.request.POST.get('password'))
        if user is not None:
            auth_login(self.request, user)
            context = super(UserLoginView, self).form_valid(form)
            context['success'] = True
            return context
        return render(self.request, self.template_name, {'form':form, 'user_error':self.user_error})


def registration(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        user = User.objects.create_user(username = username, email = email, password = password)
    return HttpResponseRedirect('/')


#def login(request):

#    if request.method == 'POST':
#        username = request.POST.get('user_name')
#        password = request.POST.get('auth_password')
#        user = authenticate(username=username, password=password)
#        if user is not None:
#            auth_login(request, user)
#    return HttpResponseRedirect('/')


#class UserLoginView(FormView):

#    form_class = UserAuthForm()

#    def form_valid(self, form_class):
#        auth_login(self.request, form_class.get_user())
#        return HttpResponseRedirect('/')

#    def form_invalid(self, form_class):
#        return render_to_response(self.get_context_date(form = form_class))



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
