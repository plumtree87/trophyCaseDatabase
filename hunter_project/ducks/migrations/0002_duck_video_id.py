# Generated by Django 3.1.7 on 2021-06-06 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ducks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='duck',
            name='video_id',
            field=models.CharField(default=None, max_length=50),
        ),
    ]