# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 18:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spartan', '__first__'),
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('text', models.CharField(max_length=500, null=True)),
                ('slug', models.SlugField(default=uuid.uuid1, unique=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('country', models.TextField(max_length=50, null=True)),
                ('city', models.TextField(max_length=100, null=True)),
                ('data', models.DateField(null=True, verbose_name='Task-ul trebuie indeplinit in data de')),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('timePost', models.TimeField(null=True, verbose_name='Ora')),
                ('money', models.IntegerField(null=True)),
                ('pret', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('employer_done', models.BooleanField(default=False)),
                ('spartan_done', models.BooleanField(default=False)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('spartan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anunturi', to='spartan.Spartan')),
            ],
            options={
                'get_latest_by': 'creation_date',
            },
        ),
    ]
