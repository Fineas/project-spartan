# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-01 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20160623_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.CharField(max_length=999),
        ),
    ]
