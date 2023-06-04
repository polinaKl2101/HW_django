from django.db import models


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

    def __str__(self):
        return f"Наименование: {self.product_name}. " \
               f"Категория: {self.category}. " \
               f"Цена за покупку: {self.price}. " \
               f"Дата создания: {self.date_created}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('pk',)