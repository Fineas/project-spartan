# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useractions', '0005_announcement_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='time',
        ),
        migrations.AddField(
            model_name='announcement',
            name='timePost',
            field=models.TimeField(null=True, verbose_name='Ora'),
        ),
    ]
