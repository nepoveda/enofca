# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-27 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import encyclopedia.models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0005_auto_20180827_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='seedbank',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=encyclopedia.models.seed_bank_upload),
        ),
        migrations.AlterField(
            model_name='strainphoto',
            name='photo',
            field=models.ImageField(upload_to=encyclopedia.models.strain_directory_upload),
        ),
    ]
