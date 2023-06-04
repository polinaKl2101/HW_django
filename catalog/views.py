from django.shortcuts import render


def homepage(request):
    return render(request, 'catalog/homepage.html')


def contacts(request):
    return render(request, 'catalog/contacts.html')

