# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20170505_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='available_time',
        ),
        migrations.AddField(
            model_name='staff',
            name='end_time',
            field=models.DateTimeField(default='2016-01-01 10:20:05.123'),
        ),
        migrations.AddField(
            model_name='staff',
            name='start_time',
            field=models.DateTimeField(default='2016-01-01 10:20:05.123'),
        ),
    ]
