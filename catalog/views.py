from django.shortcuts import render

from catalog.models import Product


def homepage(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Магазин'
    }
    return render(request, 'catalog/product.html', context=context)


def contacts(request):
    extra_context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html')


def current_prod(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/homepage.html', context)
