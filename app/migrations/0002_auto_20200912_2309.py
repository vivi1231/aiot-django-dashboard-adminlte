# Generated by Django 2.2.10 on 2020-09-12 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'get_latest_by': 'time', 'ordering': ['-time', 'in_out']},
        ),
    ]
