# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django                  import forms
from django.contrib          import admin
from django_summernote.admin import SummernoteModelAdmin
from encyclopedia.models                 import Strain, SeedBank, StrainPhoto, History, Revard


# Register your models here.
class  StrainForm(forms.ModelForm):

    class Meta:
        model = Strain
        fields = '__all__'
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

class SeedBankModelAdmin(admin.ModelAdmin):
    model = SeedBank
    search_fields = ('name',)

class RevardModelAdmin(admin.ModelAdmin):
    model = Revard
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
admin.site.register(Revard, RevardModelAdmin)
