# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-18 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0012_auto_20180914_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seedbank',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
