# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/post_images'),
        ),
    ]
