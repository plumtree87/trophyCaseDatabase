# Generated by Django 3.1.7 on 2021-06-10 21:38

from django.db import migrations, models
import ducks.models


class Migration(migrations.Migration):

    dependencies = [
        ('ducks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duck',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=ducks.models.upload_to),
        ),
    ]
