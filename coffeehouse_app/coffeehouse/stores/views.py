from django.shortcuts import render


def detail(request, store_id='1'):
    # Access store_id with 'store_id' variable
    return render(request, 'stores/detail.html')