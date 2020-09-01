# Generated by Django 3.1 on 2020-09-01 19:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 1, 22, 27, 36, 667481))),
                ('text', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='blog_images/')),
            ],
        ),
    ]
