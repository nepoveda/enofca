# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 11:58
from __future__ import unicode_literals

from django.db import migrations, models
import encyclopedia.models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0025_auto_20181027_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=encyclopedia.models.history_upload_to),
        ),
    ]