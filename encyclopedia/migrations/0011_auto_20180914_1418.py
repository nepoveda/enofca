# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-14 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0010_remove_strain_relaxed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='strain',
            name='anorexia',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='choding_feeling',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='communication',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='creativ',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='depression',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='dry_eyes',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='dry_mouth',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='headache',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='indica',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='insomnia',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='medicinal_mixtures',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='pain',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='paranoia',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='pozitiv_emotion',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='relax',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='sativa',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='strain',
            name='stress',
            field=models.PositiveSmallIntegerField(blank=True, default=1),
        ),
    ]
