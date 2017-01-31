# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-30 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('mobile_num', models.CharField(max_length=11)),
                ('attendance', models.CharField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsor_name', models.CharField(blank=True, max_length=400)),
                ('sponsor_email', models.EmailField(max_length=100)),
                ('sponsor_image', models.FileField(upload_to='sponsors/%Y/%m/%d')),
            ],
        ),
    ]
