# Generated by Django 2.2.10 on 2020-09-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200913_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='face',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
