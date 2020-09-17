# Generated by Django 3.1.1 on 2020-09-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Id', models.IntegerField(blank=True, null=True)),
                ('User_name', models.CharField(max_length=100)),
                ('User_email', models.CharField(max_length=200, unique=True)),
                ('User_password', models.CharField(max_length=100)),
                ('User_address', models.CharField(max_length=200)),
                ('User_phone', models.IntegerField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
