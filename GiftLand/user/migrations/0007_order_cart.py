# Generated by Django 3.1.1 on 2020-09-19 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0007_auto_20200919_2134'),
        ('user', '0006_remove_order_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Product.cart'),
        ),
    ]
