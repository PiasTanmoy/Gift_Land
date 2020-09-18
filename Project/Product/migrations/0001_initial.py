# Generated by Django 3.1.1 on 2020-09-17 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.IntegerField(blank=True, null=True)),
                ('cart_status', models.CharField(max_length=100)),
                ('cart_time', models.DateTimeField(auto_now_add=True)),
                ('cart_discount', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(blank=True, null=True)),
                ('category_type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(blank=True, null=True)),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.IntegerField(blank=True, null=True)),
                ('product_totalstock', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(blank=True, null=True)),
                ('review_rating', models.CharField(max_length=100)),
                ('review_comment', models.CharField(max_length=200)),
            ],
        ),
    ]
