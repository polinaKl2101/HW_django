# Generated by Django 4.2.1 on 2023-07-01 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Страна'),
        ),
    ]