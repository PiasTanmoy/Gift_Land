# Generated by Django 3.1.1 on 2020-09-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductView', '0002_auto_20200925_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(upload_to='picture/'),
        ),
    ]