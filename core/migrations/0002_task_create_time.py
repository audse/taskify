# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-16 09:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
