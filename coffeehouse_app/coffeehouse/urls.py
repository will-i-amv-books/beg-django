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


urlpatterns = [
    url(r'^admin/doc/$', include('django.contrib.admindocs.urls')),
    url(r'^admin/$', admin.site.urls),
    url(r'^about/', include('coffeehouse.about.urls', namespace="about")), 
    url(r'^stores/', include('coffeehouse.stores.urls', namespace="stores"), {'location':'headquarters'}), 
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage"), 
    url(r'^coffeebanners/', include('coffeehouse.banners.urls', namespace="coffee-banners")), 
    url(r'^teabanners/', include('coffeehouse.banners.urls', namespace="tea-banners")), 
    url(r'^foodbanners/', include('coffeehouse.banners.urls', namespace="food-banners")), 
    url(
        r'^drinks/(?P<drink_name>\D+)/', 
        TemplateView.as_view(template_name='drinks/index.html'),
        {'onsale':True},
        name="drink",
    ),
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name="homepage")
]
