from django.shortcuts import render

from catalog.models import Product
from django.views import generic


class HomepageListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Магазин'
    }


class Current_prodDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


# def current_prod(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list
#     }
#     return render(request, 'catalog/homepage.html', context)


# class ContactsListView(generic.ListView):
#     model = Product
#      extra_context = {
#          'title': 'Контакты'
#      }

def contacts(request):
    extra_context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contact.html')



