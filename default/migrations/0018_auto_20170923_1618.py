# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0017_auto_20170923_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='track_id',
        ),
        migrations.AlterField(
            model_name='submission',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Conference'),
        ),
    ]
