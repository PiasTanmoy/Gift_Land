# Generated by Django 3.1 on 2020-09-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0002_auto_20200918_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.IntegerField(blank=True, null=True)),
                ('admin_name', models.CharField(max_length=100)),
                ('admin_email', models.CharField(max_length=200, unique=True)),
                ('admin_phone', models.IntegerField(blank=True, null=True)),
                ('product', models.ManyToManyField(to='Product.Product')),
            ],
        ),
    ]
