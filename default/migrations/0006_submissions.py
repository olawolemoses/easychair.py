# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-18 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0005_user_photourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='submissions',
            fields=[
                ('id', models.AutoField(help_text='reviewer', primary_key=True, serialize=False)),
                ('conference_id', models.IntegerField(help_text='conference', max_length=20, unique=True)),
                ('user_id', models.IntegerField(help_text='user ID', max_length=20, unique=True)),
                ('track_id', models.IntegerField(help_text='track', max_length=20, unique=True)),
                ('title', models.CharField(help_text='Enter a title', max_length=200)),
                ('abstract', models.TextField(help_text='Enter a abstract')),
                ('keywords', models.CharField(help_text='keywords', max_length=200)),
                ('paper_url', models.CharField(help_text='paper url', max_length=200)),
                ('status', models.CharField(help_text='status', max_length=200)),
            ],
        ),
    ]