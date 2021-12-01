"""coffeehouse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from coffeehouse.drinks.urls import urlpatterns as drinks_url_patterns


# Overrides the default 400 handler django.views.defaults.bad_request
handler400 = 'coffeehouse.utils.views.bad_request'
# Overrides the default 403 handler django.views.defaults.permission_denied
handler403 = 'coffeehouse.utils.views.permission_denied'
# Overrides the default 404 handler django.views.defaults.page_not_found
handler404 = 'coffeehouse.utils.views.page_not_found'
# Overrides the default 500 handler django.views.defaults.server_error
handler500 = 'coffeehouse.utils.views.server_error'
    
urlpatterns = [
    url(r'^admin/doc/',  include('django.contrib.admindocs.urls')), 
    url(r'^admin/',  admin.site.urls), 
    url(r'^about/', include('coffeehouse.about.urls', namespace="about")), 
    url(r'^stores/', include('coffeehouse.stores.urls', namespace="stores")), 
    url(r'^drinks/', include(drinks_url_patterns, namespace="drinks")),
    url(r'^coffeebanners/', include('coffeehouse.banners.urls', namespace="coffee-banners", app_name="banners_adverts")), 
    url(r'^online/',TemplateView.as_view(template_name='online/index.html'),name='online'),
    url(r'^teabanners/', include('coffeehouse.banners.urls', namespace="tea-banners", app_name="banners_adverts")), 
    url(r'^foodbanners/', include('coffeehouse.banners.urls', namespace="food-banners", app_name="banners_adverts")), 
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"), 
]
