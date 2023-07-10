from django.contrib import admin
from catalog.models import Product, Category, BlogPost, Client, Message, Mailing, Log


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('message', 'timedata', 'status')
    list_filter = ('message', 'timedata', 'status')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('title', 'frequency', 'status')
    list_filter = ('frequency', 'status')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'message')
    list_filter = ('title', 'message')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fullname')
    list_filter = ('email', 'fullname')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category', 'is_published')
    list_filter = ('category',)
    search_fields = ('product_name', 'description',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'slug')

