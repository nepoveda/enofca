# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-01 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0027_auto_20181029_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='strain',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]