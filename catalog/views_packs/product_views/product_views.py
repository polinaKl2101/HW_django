from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version
from django.forms import inlineformset_factory


class Current_ProductDetailView(generic.DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']
        return context_data


class ProductCreateView(LoginRequiredMixin, generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:homepage')
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:homepage')
    permission_required = 'catalog.change_product'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        context_data['formset'] = VersionFormset()
        return context_data

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        if (self.request.user != kwargs['instance'].user) or (not self.request.user.has_perm('catalog.change_product')):
            return self.handle_no_permission()

        return kwargs


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'post'
    success_url = reverse_lazy('catalog:homepage')

    def get_queryset(self):
        return Product.objects


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:current_prod')
    permission_required = 'catalog.delete_product'
