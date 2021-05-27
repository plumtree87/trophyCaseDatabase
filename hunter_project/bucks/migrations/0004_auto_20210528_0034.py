# Generated by Django 3.1.7 on 2021-05-27 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bucks', '0003_auto_20210527_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buck',
            name='documentsUpload',
        ),
        migrations.RemoveField(
            model_name='buck',
            name='imageUpload',
        ),
        migrations.AlterField(
            model_name='buck',
            name='documents',
            field=models.FileField(blank=True, default=None, null=True, upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='buck',
            name='image',
            field=models.ImageField(default=None, upload_to='buckImages/'),
        ),
    ]