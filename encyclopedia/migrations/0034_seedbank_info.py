# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-10 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0033_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='seedbank',
            name='info',
            field=models.TextField(blank=True, verbose_name='informace'),
        ),
    ]
