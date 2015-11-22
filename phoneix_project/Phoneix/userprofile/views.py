from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePage(TemplateView):

    template_name = 'index.html'

class HospitalsPageview(TemplateView):

    template_name = 'hospitals.html'

class ClinicsPageView(TemplateView):

    template_name = 'clinics.html'

class DgLabsPageView(TemplateView):

    template_name = 'dglabs.html'

class PharmacyPageview(TemplateView):

    template_name = 'pharmacy.html'

class ContactPageView(TemplateView):

    template_name = 'contact.html'

