from django import forms

from catalog.models import Product, Version, BlogPost, Client, Message, Mailing, Log


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ['email', 'fullname', 'comment']


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ('title', 'message')


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = ['title', 'frequency', 'status', 'clients']


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'preview', 'is_published']


class StyleFormMixin:
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['product_name', 'description', 'image', 'category', 'price', 'is_published']


    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('product_name')
        description = cleaned_data.get('description')

        if name and any(word in name.lower() for word in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']):
            raise forms.ValidationError("Название продукта содержит запрещенные слова.")

        if description and any(word in description.lower() for word in ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']):
            raise forms.ValidationError("Описание продукта содержит запрещенные слова.")

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    version_number = forms.IntegerField(label='Номер версии')
    version_name = forms.CharField(label='Название версии', max_length=100)

    class Meta:
        model = Version
        fields = '__all__'