# Generated by Django 3.1.1 on 2020-09-19 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0006_cart_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='orders',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='users',
        ),
    ]
