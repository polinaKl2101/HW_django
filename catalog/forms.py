from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('product_name', 'description', 'image', 'category', 'price')
        # exclude = ('date_created')

