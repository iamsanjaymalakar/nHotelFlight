# Generated by Django 2.2.3 on 2019-08-18 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20190818_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='Percentage',
            field=models.FloatField(),
        ),
    ]