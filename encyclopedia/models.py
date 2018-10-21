# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Strain(models.Model):
    name = models.CharField(u'název', max_length=100)
    info = models.TextField(u'informace', blank=True)
    bank = models.ForeignKey('SeedBank', on_delete=models.SET_NULL, null=True, blank=True)
    revard = models.ForeignKey('Revard', on_delete=models.SET_NULL, null=True, blank=True)
    webId = models.SlugField(max_length=50, unique=True)

    #basic information
    sativa = models.PositiveSmallIntegerField(blank=True, default=1)
    indica = models.PositiveSmallIntegerField(blank=True, default=1)

    #effects
    creativ = models.PositiveSmallIntegerField(blank=True, default=1)
    relax = models.PositiveSmallIntegerField(blank=True, default=1)
    communication = models.PositiveSmallIntegerField(blank=True, default=1)
    pozitiv_emotion = models.PositiveSmallIntegerField(blank=True, default=1)

    #medical
    medicinal_mixtures = models.PositiveSmallIntegerField(blank=True, default=1)
    anorexia = models.PositiveSmallIntegerField(blank=True, default=1)
    insomnia = models.PositiveSmallIntegerField(blank=True, default=1)
    pain = models.PositiveSmallIntegerField(blank=True, default=1)
    stress = models.PositiveSmallIntegerField(blank=True, default=1)
    depression = models.PositiveSmallIntegerField(blank=True, default=1)

    #negatives
    dry_eyes = models.PositiveSmallIntegerField(blank=True, default=1)
    paranoia = models.PositiveSmallIntegerField(blank=True, default=1)
    dry_mouth = models.PositiveSmallIntegerField(blank=True, default=1)
    choding_feeling = models.PositiveSmallIntegerField(blank=True, default=1)
    headache = models.PositiveSmallIntegerField(blank=True, default=1)

    def __str__(self):
        return '{} - {}'.format(self.name, self.webId)

def seed_bank_upload(instance, filename):
    return 'banks/{0}/{1}'.format(instance.name, filename)

class SeedBank(models.Model):
    logo = models.ImageField(upload_to=seed_bank_upload, blank=True, null=True)
    name = models.CharField(max_length=100)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

def revard_upload(instance, filename):
    return 'revards/{0}/{1}'.format(instance.name, filename)

class Revard(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=revard_upload, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

def strain_directory_upload(instance, filename):
    return 'strains/{0}/{1}'.format(instance.strain.name, filename)

class StrainPhoto(models.Model):
    photo = models.ImageField(upload_to=strain_directory_upload)
    strain = models.ForeignKey('Strain', on_delete=models.SET_NULL, null=True, blank=True)

HISTORY_CHOICES = (
    ('1900', 'before 1900'),
    ('2000', '1900 - 2000'),
    ('now', '2000 - now'),
)

def history_upload_to(instance, filename):
    return 'history/{0}/{1}/{2}'.format(instance.period, instance.header, filename)

class History(models.Model):
    period = models.CharField(max_length=10, choices = HISTORY_CHOICES)
    header = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to=history_upload_to, blank=True, null=True)
    standing = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} - {}'.format(self.period, self.header)
