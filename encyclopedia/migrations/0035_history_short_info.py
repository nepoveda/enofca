# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-01 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0034_seedbank_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='short_info',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]