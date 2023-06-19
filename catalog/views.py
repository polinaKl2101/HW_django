from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView

from catalog.forms import ProductForm, VersionForm, BlogPostForm
from catalog.models import Product, BlogPost, Version
from django.views import generic
from django.urls import reverse_lazy


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


class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = 'catalog/blogpost_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'catalog/blogpost_detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class BlogPostCreateView(generic.CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'catalog/blogpost_form.html'
    fields = ['title', 'content', 'preview', 'is_published']


class BlogPostUpdateView(UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse_lazy('catalog:blog_post', kwargs={'slug': self.object.slug})


class BlogPostDeleteView(generic.DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()
        return context_data


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
    return render(request, 'catalog/change_version.html', {'form': form, 'product': product})


# class BlogPostUpdateView(generic.UpdateView):
#     model = BlogPost
#     template_name = 'catalog/blogpost_form.html'
#     fields = ['title', 'content', 'preview', 'is_published']
#
#     def get_success_url(self):
#         return reverse_lazy('blogpost_detail', kwargs={'slug': self.object.slug})



