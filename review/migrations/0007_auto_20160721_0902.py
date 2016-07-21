# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-21 09:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20160721_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='data',
            field=models.DateField(default=datetime.datetime(2016, 7, 21, 9, 2, 49, 359505, tzinfo=utc), null=True, verbose_name='Review publication day'),
        ),
    ]
