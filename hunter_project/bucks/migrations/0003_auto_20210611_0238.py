# Generated by Django 3.1.7 on 2021-06-10 21:38

import bucks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucks', '0002_auto_20210610_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buck',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=bucks.models.upload_to),
        ),
    ]
