from django.db.models import Count
from django.shortcuts import render, redirect
from catalog.forms import VersionForm
from catalog.models import Product, BlogPost, Version, Client, Mailing
from django.views import generic


class HomepageListView(generic.ListView):
    model = Product
    extra_context = {
        'title': 'Магазин'
    }


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'catalog/index.html', context)


def get(self, request, *args, **kwargs):
    mailing_number = Mailing.objects.count()
    mailing_number_active = Mailing.objects.filter(
        status='started').count()
    unique_clients = Client.objects.annotate(mailing_num=Count('mailing')).filter(
        mailing_num__gt=0).count()
    blogpost = list(BlogPost.objects.filter(is_active=True).order_by('?').values_list('title', flat=True)[
                      :3])
    context = {
        'title': 'Главная',
        'mailing_number': mailing_number,
        'mailing_number_active': mailing_number_active,
        'unique_clients': unique_clients,
        'blogpost': blogpost
    }
    return render(request, 'catalog/index.html', context)


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
            new_version = Version(product=product, version_number=new_version_number, version_name=new_version_name,
                                  is_active=True)
            new_version.save()
            return redirect('catalog:homepage')
    else:
        form = VersionForm()
    return render(request, 'catalog/contacts/change_version.html', {'form': form, 'product': product})
