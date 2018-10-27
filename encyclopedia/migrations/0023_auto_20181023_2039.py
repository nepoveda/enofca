# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-23 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import encyclopedia.models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0022_auto_20181021_2256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CupPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=encyclopedia.models.revard_upload)),
                ('cup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='encyclopedia.Cup')),
            ],
        ),
        migrations.CreateModel(
            name='Revadr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='strain',
            name='revard',
        ),
        migrations.DeleteModel(
            name='Revard',
        ),
        migrations.AddField(
            model_name='strain',
            name='cup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='encyclopedia.Cup'),
        ),
    ]