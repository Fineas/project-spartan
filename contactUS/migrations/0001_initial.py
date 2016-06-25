# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=1000, null=True)),
            ],
        ),
    ]
