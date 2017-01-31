# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-31 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20170130_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='Sponsors',
            new_name='Sponsor',
        ),
    ]
