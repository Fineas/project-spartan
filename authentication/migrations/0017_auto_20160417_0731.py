# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-17 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0016_auto_20160417_0617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='country',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]