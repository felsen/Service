"""Phoneix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

# django imports.
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

# local file imports.
import settings
from userprofile.views import HomePage, HospitalsListView, ClinicsPageView, DgLabsPageView, \
    PharmacyPageview, ContactPageView, HospitalPageView, UserLoginView, UserRegistrationView, \
    AboutUsPageview, TermsServicePageview, BlogPageview

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Logout url accessing django in-built logout functions.
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),

    # User Profile App Urls:
    url(r'^$', HomePage.as_view(), name = 'home-page'),
    url(r'^hospitals-list/$', HospitalsListView.as_view(), name = 'hospitals-list'),
    url(r'^clinics-list/$', ClinicsPageView.as_view(), name = 'clinics-page'),
    url(r'^dglabs-list/$', DgLabsPageView.as_view(), name = 'dglabspage'),
    url(r'^pharmacy-list/$', PharmacyPageview.as_view(), name = 'pharmacy-page'),
    url(r'^about-us/$', AboutUsPageview.as_view(), name = 'about-us-page'),
    url(r'^terms-of-services/$', TermsServicePageview.as_view(), name = 'terms-of-page'),
    url(r'^blog/$', BlogPageview.as_view(), name = 'blog-page'),
    
    url(r'^contact-page/$', ContactPageView.as_view(), name = 'contact-page'),
    url(r'^hospital-page/$', HospitalPageView.as_view(), name = 'hospital-page'),
    url(r'^user-registration/$', UserRegistrationView.as_view(), name = 'user-registration'),
    url(r'^user-login/$', UserLoginView.as_view(), name = 'user-login'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





