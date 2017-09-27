# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-23 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0018_auto_20170923_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(help_text='reviewer', primary_key=True, serialize=False)),
                ('fname', models.CharField(help_text='name of conference', max_length=100)),
                ('lname', models.CharField(help_text='name of conference', max_length=100)),
                ('email', models.CharField(help_text='name of conference', max_length=200)),
                ('org', models.CharField(help_text='name of conference', max_length=200, null=True)),
                ('speaker', models.NullBooleanField(default=True, help_text='speaker', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Correspondence',
            fields=[
                ('id', models.AutoField(help_text='reviewer', primary_key=True, serialize=False)),
                ('address1', models.CharField(help_text='name of conference', max_length=200)),
                ('address2', models.CharField(help_text='name of conference', max_length=200)),
                ('city', models.CharField(help_text='name of conference', max_length=200)),
                ('state', models.CharField(help_text='name of conference', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(help_text='reviewer', primary_key=True, serialize=False)),
                ('country', models.CharField(help_text='name of conference', max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='conference',
            name='country_id',
            field=models.IntegerField(help_text='country'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='conference',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Conference'),
        ),
        migrations.AddField(
            model_name='correspondence',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Country'),
        ),
        migrations.AddField(
            model_name='correspondence',
            name='submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Submission'),
        ),
        migrations.AddField(
            model_name='author',
            name='country',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Country'),
        ),
        migrations.AddField(
            model_name='author',
            name='submission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='default.Submission'),
        ),
    ]
