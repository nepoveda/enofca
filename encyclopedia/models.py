# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Strain(models.Model):
    name = models.CharField(u'název', max_length=100)
    info = models.TextField(u'informace')
    bank = models.ForeignKey('SeedBank', on_delete=models.SET_NULL, null=True, blank=True)
    webId = models.PositiveIntegerField()

    #basic information
    sativa = models.PositiveSmallIntegerField()
    indica = models.PositiveSmallIntegerField()

    #effects
    creativ = models.PositiveSmallIntegerField()
    relax = models.PositiveSmallIntegerField()
    communication = models.PositiveSmallIntegerField()
    pozitiv_emotion = models.PositiveSmallIntegerField()

    #medical
    medicinal_mixtures = models.PositiveSmallIntegerField()
    anorexia = models.PositiveSmallIntegerField()
    insomnia = models.PositiveSmallIntegerField()
    pain = models.PositiveSmallIntegerField()
    stress = models.PositiveSmallIntegerField()
    depression = models.PositiveSmallIntegerField()

    #negatives
    dry_eyes = models.PositiveSmallIntegerField()
    paranoia = models.PositiveSmallIntegerField()
    dry_mouth = models.PositiveSmallIntegerField()
    choding_feeling = models.PositiveSmallIntegerField()
    headache = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.webId)

def seed_bank_upload(instance, filename):
    return 'banks/{0}/{1}'.format(instance.name, filename)

class SeedBank(models.Model):
    logo = models.ImageField(upload_to=seed_bank_upload, blank=True, null=True)
    name = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return '{}'.format(self.name)

class Revard(models.Model):
    name = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField()

def strain_directory_upload(instance, filename):
    return 'strains/{0}/{1}'.format(instance.strain.name, filename)

class StrainPhoto(models.Model):
    photo = models.ImageField(upload_to=strain_directory_upload)
    strain = models.ForeignKey('Strain', on_delete=models.SET_NULL, null=True, blank=True)
