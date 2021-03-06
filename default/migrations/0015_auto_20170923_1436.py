# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 14:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0014_auto_20170923_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='user_id',
        ),
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='submission',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Conference'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='track_id',
            field=models.IntegerField(help_text='track', unique=True),
        ),
    ]
