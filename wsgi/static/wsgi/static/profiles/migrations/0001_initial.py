# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 23:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, max_length=2048)),
                ('birthDate', models.DateField(null=True, verbose_name='birthDate')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('image', models.ImageField(blank=True, upload_to='media/profile_images')),
                ('city', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('address', models.CharField(max_length=128)),
                ('postalCode', models.CharField(max_length=7)),
                ('phoneNumber', models.CharField(max_length=30)),
                ('user', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
