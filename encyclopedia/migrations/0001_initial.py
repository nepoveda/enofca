# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-03 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='n\xe1zev')),
                ('info', models.TextField(verbose_name='informace')),
            ],
        ),
        migrations.CreateModel(
            name='SeedBank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='n\xe1zev')),
                ('link', models.CharField(max_length=100, verbose_name='link')),
            ],
        ),
    ]
