# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-21 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0031_auto_20181121_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strain',
            name='cup_place',
            field=models.PositiveSmallIntegerField(blank=True, default=None, null=True),
        ),
    ]