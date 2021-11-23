from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect
from django.core.urlresolvers import reverse


def contact(request):
    # Content from request or database extracted here
    # and passed to the template for display
    return HttpResponsePermanentRedirect(reverse('stores:about:index'))