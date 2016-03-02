# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 09:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('city', models.CharField(max_length=40)),
                ('country', models.CharField(max_length=30, null=True)),
                ('telefon', models.IntegerField(null=True)),
                ('photo', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]