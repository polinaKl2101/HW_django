# Generated by Django 4.2.1 on 2023-06-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
    ]