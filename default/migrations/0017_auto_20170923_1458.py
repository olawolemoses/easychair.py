# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0016_auto_20170923_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Conference'),
        ),
    ]
