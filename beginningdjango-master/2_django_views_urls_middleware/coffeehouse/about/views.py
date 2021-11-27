# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from coffeehouse.stores.views import STORE_LIST
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, Http404


def index(request, store_id=None):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    if store_id == None:
        store = STORE_LIST[0]
    elif store_id == "1":
        store = STORE_LIST[1]
    elif store_id == "2":
        store = STORE_LIST[2]
    elif store_id == "3":
        store = STORE_LIST[3]
    else:
        raise Http404
    return render(request, 'about/index.html', {'store':store})


class ContactPage(View):
    mytemplate = 'about/contact.html'
    unsupported = 'Unsupported operation'
    
    def get(self,  request, store_id=None):
        # Create fixed data structures to pass to template
        # data could equally come from database queries
        if store_id == None:
            store = STORE_LIST[0]
        elif store_id == "1":
            store = STORE_LIST[1]
        elif store_id == "2":
            store = STORE_LIST[2]
        elif store_id == "3":
            store = STORE_LIST[3]
        else:
            raise Http404        
        return render(request,  self.mytemplate, {'store':store})

    def post(self,  request):
        return HttpResponse(self.unsupported)
