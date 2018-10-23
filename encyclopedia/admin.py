# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django                  import forms
from django.contrib          import admin
from django_summernote.admin import SummernoteModelAdmin
from encyclopedia.models                 import Strain, SeedBank, StrainPhoto, History, Cup, CupPhoto


# Register your models here.
class  StrainForm(forms.ModelForm):

    class Meta:
        model = Strain
        fields = ('name', 'webId', 'info', 'bank', 'cup', 'stress', 'insomnia', 'pain',
                  'depression', 'headaches', 'lack_of_appetite', 'muscle_spams', 'nausea', 'cramps',
                  'fatigue', 'inflammation', 'communicative', 'creative', 'energetic',  'euphoric',
                  'focused', 'happy', 'relaxed', 'uplifted', 'talkative', 'aroused', 'giggly',
                  'dry_eyes', 'dry_mouth', 'headache', 'paranoid', 'dizzy', 'anxious')
        widgets = {
            'name': forms.widgets.TextInput(attrs={'style': 'width:90%;'}),
            'webId': forms.widgets.NumberInput()
        }

class StrainPhotoModelAdmin(admin.ModelAdmin):
    pass

class StrainPhotoInline(admin.StackedInline):
    model = StrainPhoto
    max_num = 20
    extra = 3

class StrainModelAdmin(SummernoteModelAdmin):
    form = StrainForm
    inlines = [StrainPhotoInline,]
    search_fields = ('name', 'webId')

class  CupForm(forms.ModelForm):

    class Meta:
        model = Cup
        fields = '__all__'

class CupPhotoModelAdmin(admin.ModelAdmin):
    pass

class CupPhotoInline(admin.StackedInline):
    model = CupPhoto
    max_num = 20
    extra = 3

class CupModelAdmin(admin.ModelAdmin):
    form = CupForm
    inlines = [CupPhotoInline,]

class SeedBankModelAdmin(admin.ModelAdmin):
    model = SeedBank
    search_fields = ('name',)

class  HistoryForm(forms.ModelForm):

    class Meta:
        model = Strain
        fields = '__all__'
        widgets = {
            'text': forms.widgets.TextInput(attrs={'style': 'width:90%;'}),
        }

class HistoryModelAdmin(SummernoteModelAdmin):
    form = HistoryForm

admin.site.register(Strain, StrainModelAdmin)
admin.site.register(SeedBank, SeedBankModelAdmin)
admin.site.register(History, HistoryModelAdmin)
admin.site.register(Cup, CupModelAdmin)
