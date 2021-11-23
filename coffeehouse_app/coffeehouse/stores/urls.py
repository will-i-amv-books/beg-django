# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include,  url
from . import views 


urlpatterns = [
    url(r'^(?P<store_id>\d+)/about/', include('coffeehouse.about.urls', namespace="about")), 
    url(r'^(?P<store_id>\d+)/$', views.detail, name="detail"), 
    url(r'^$', views.index, name="index"), 
]

