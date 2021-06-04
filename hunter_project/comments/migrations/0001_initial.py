# Generated by Django 3.1.7 on 2021-06-04 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(blank=True, max_length=1000)),
                ('like', models.BooleanField(default=False)),
                ('dislike', models.BooleanField(default=False)),
            ],
        ),
    ]
