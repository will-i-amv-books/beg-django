from django.shortcuts import render


def detail(request, store_id='1', location=None):
    # Access store_id with 'store_id' variable
    return render(request, 'stores/detail.html')