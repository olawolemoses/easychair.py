# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-14 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0002_auto_20170914_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aboutme',
            field=models.TextField(blank=True, null=True),
        ),
    ]