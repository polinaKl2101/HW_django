from django.conf import settings
from django.db import models
from django.utils.text import slugify
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Клиент сервиса"""

    email = models.EmailField(unique=True, verbose_name='Контактный email')
    fullname = models.CharField(max_length=255, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Mailing(models.Model):
    """Рассылка (настройки)"""

    FREQUENCY_CHOICES = (
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    )
    STATUS_CHOICES = (
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('completed', 'Завершена'),
    )

    title = models.CharField(max_length=60, verbose_name='Тема рассылки')
    body = models.TextField(verbose_name='Тело письма')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='created', verbose_name='Статус рассылки')
    clients = models.ManyToManyField('Client', verbose_name='Клиенты')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    """Сообщение для рассылки"""

    title = models.CharField(max_length=60, verbose_name='Тема письма')
    message = models.ForeignKey(Mailing, verbose_name='Рассылка', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Log(models.Model):
    """Модель Логи рассылки"""

    STATUS_CHOICES = (
        ('success', 'Успешно'),
        ('error', 'Ошибка'),
    )

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение для рассылки')
    timedata = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время последней попытки')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, verbose_name='Статус попытки')
    server_response = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)

    def __str__(self):
        return f"Время последней рассылки: {self.timedata}"

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'


class Category(models.Model):

    category_name = models.CharField(max_length=150, verbose_name='Название категории')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

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
    is_published = models.BooleanField(default=False)


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