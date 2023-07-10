from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, BlogPostForm, ClientForm
from catalog.models import Product, BlogPost, Version, Client
from django.views import generic
from django.urls import reverse_lazy


class HomepageListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Магазин'
    }

class Current_ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


def contacts(request):
    extra_context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts/contact.html')


def change_version(request, product_id):
    product = Product.objects.get(id=product_id)
    active_version = product.versions.filter(is_active=True).first()
    if request.method == 'POST':
        form = VersionForm(request.POST)
        if form.is_valid():
            new_version_number = form.cleaned_data['version_number']
            new_version_name = form.cleaned_data['version_name']
            if active_version:
                active_version.is_active = False
                active_version.save()
            new_version = Version(product=product, version_number=new_version_number, version_name=new_version_name, is_active=True)
            new_version.save()
            return redirect('product_list')
    else:
        form = VersionForm()
    return render(request, 'catalog/contacts/change_version.html', {'form': form, 'product': product})




