from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from catalog.forms import ProductForm
from catalog.models import Product, BlogPost
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
    extra_context = {'title': 'список постов'}


class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'catalog/blogpost_form.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')

# class BlogPostCreateView(generic.CreateView):
#     model = BlogPost
#     template_name = 'catalog/blogpost_form.html'
#     fields = ['title', 'content', 'preview', 'is_published']


# class BlogPostUpdateView(generic.UpdateView):
#     model = BlogPost
#     template_name = 'catalog/blogpost_form.html'
#     fields = ['title', 'content', 'preview', 'is_published']
#
#     def get_success_url(self):
#         return reverse_lazy('blogpost_detail', kwargs={'slug': self.object.slug})


# class BlogPostDeleteView(generic.DeleteView):
#     model = BlogPost
#     template_name = 'blogpost_confirm_delete.html'
#     success_url = reverse_lazy('blogpost_list')
