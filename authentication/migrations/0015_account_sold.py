# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-15 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_spartan_spartanstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='sold',
            field=models.IntegerField(default=1000),
        ),
    ]
