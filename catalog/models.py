from django.conf import settings
from django.db import models
from django.utils.text import slugify
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):

    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('pk',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена за покупку')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    last_change_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')


    def __str__(self):
        return f"Наименование: {self.product_name}. " \
               f"Категория: {self.category}. " \
               f"Цена за покупку: {self.price}. " \
               f"Дата создания: {self.date_created}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.CharField(max_length=200, null=True, blank=True, unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', verbose_name='Изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Version(models.Model):

    version_number = models.IntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    version_flag = models.TextField(verbose_name='признак текущей версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return {self.version_name}

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'