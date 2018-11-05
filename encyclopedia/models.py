# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Strain(models.Model):
    name = models.CharField(u'název', max_length=100)
    info = models.TextField(u'informace', blank=True)
    bank = models.ForeignKey('SeedBank', on_delete=models.SET_NULL, null=True, blank=True)
    cup = models.ManyToManyField('Cup', blank=True)
    webId = models.SlugField(max_length=50, unique=True)
    link = models.URLField(blank=True, null=True)

    #medical
    stress = models.PositiveSmallIntegerField(blank=True, default=0)
    insomnia = models.PositiveSmallIntegerField(blank=True, default=0)
    pain = models.PositiveSmallIntegerField(blank=True, default=0)
    depression = models.PositiveSmallIntegerField(blank=True, default=0)
    headaches = models.PositiveSmallIntegerField(blank=True, default=0)
    lack_of_appetite = models.PositiveSmallIntegerField(blank=True, default=0)
    muscle_spams = models.PositiveSmallIntegerField(blank=True, default=0)
    nausea = models.PositiveSmallIntegerField(blank=True, default=0)
    cramps = models.PositiveSmallIntegerField(blank=True, default=0)
    fatigue = models.PositiveSmallIntegerField(blank=True, default=0)
    inflammation = models.PositiveSmallIntegerField(blank=True, default=0)

    #effects
    communicative = models.PositiveSmallIntegerField(blank=True, default=0)
    creative = models.PositiveSmallIntegerField(blank=True, default=0)
    energetic = models.PositiveSmallIntegerField(blank=True, default=0)
    euphoric = models.PositiveSmallIntegerField(blank=True, default=0)
    focused = models.PositiveSmallIntegerField(blank=True, default=0)
    happy = models.PositiveSmallIntegerField(blank=True, default=0)
    relaxed = models.PositiveSmallIntegerField(blank=True, default=0)
    uplifted = models.PositiveSmallIntegerField(blank=True, default=0)
    talkative = models.PositiveSmallIntegerField(blank=True, default=0)
    aroused = models.PositiveSmallIntegerField(blank=True, default=0)
    giggly = models.PositiveSmallIntegerField(blank=True, default=0)

    #negatives
    dry_eyes = models.PositiveSmallIntegerField(blank=True, default=0)
    dry_mouth = models.PositiveSmallIntegerField(blank=True, default=0)
    headache = models.PositiveSmallIntegerField(blank=True, default=0)
    paranoid = models.PositiveSmallIntegerField(blank=True, default=0)
    dizzy = models.PositiveSmallIntegerField(blank=True, default=0)
    anxious = models.PositiveSmallIntegerField(blank=True, default=0)


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

#odstarnit poté z migrací
def revard_upload(instance, filename):
    return 'revards/{0}/{1}'.format(instance.name, filename)

def cup_upload(instance, filename):
    return 'cups/{0}/{1}'.format(instance.cup.name, filename)

class Revadr(models.Model):
    pass

class Cup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

class CupPhoto(models.Model):
    cup = models.ForeignKey('Cup', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to=cup_upload, blank=True, null=True)

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
    return 'history/{0}/{1}'.format(instance.period, filename)

class History(models.Model):
    period = models.CharField(max_length=10, choices = HISTORY_CHOICES)
    header = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to=history_upload_to, blank=True, null=True)
    pdf = models.FileField(upload_to=history_upload_to, blank=True, null=True)
    standing = models.PositiveSmallIntegerField()

    def __str__(self):
        return '{} - {}'.format(self.period, self.header)
