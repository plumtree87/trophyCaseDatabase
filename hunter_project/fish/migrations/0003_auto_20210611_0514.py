# Generated by Django 3.1.7 on 2021-06-11 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20210610_1016'),
        ('fish', '0002_auto_20210611_0238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bass',
            name='comments',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commentsAboutBass', to='comments.comment'),
        ),
    ]