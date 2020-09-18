# Generated by Django 3.1.1 on 2020-09-18 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='Product.Product'),
        ),
        migrations.AddField(
            model_name='category',
            name='product',
            field=models.ManyToManyField(to='Product.Product'),
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ManyToManyField(to='Product.Product'),
        ),
    ]
