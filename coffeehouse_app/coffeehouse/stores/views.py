from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse


def detail(request, store_id='1', location=None):
    # Extract 'hours' or 'map' value appended to url as ?hours=sunday&map=flash
    hours = request.GET.get('hours', '') # 'hours' has value 'sunday' or '' if hours not in url
    map = request.GET.get('map', '') # 'map' has value 'flash' or '' if map not in url
    return HttpResponsePermanentRedirect(reverse('about:detail'))