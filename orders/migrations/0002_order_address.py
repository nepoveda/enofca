# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-17 18:07
from __future__ import unicode_literals

import address.models
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20160213_1726'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=address.models.AddressField(default='', on_delete=django.db.models.deletion.CASCADE, to=b'address.Address'),
            preserve_default=False,
        ),
    ]
