# Generated by Django 2.2.3 on 2019-08-18 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0012_auto_20190818_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='Longitude',
        ),
    ]