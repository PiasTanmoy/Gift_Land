# Generated by Django 3.1.1 on 2020-09-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_auto_20200917_1214'),
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='product',
            field=models.ManyToManyField(to='Product.Product'),
        ),
    ]