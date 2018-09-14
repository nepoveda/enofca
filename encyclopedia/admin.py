# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django                  import forms
from django.contrib          import admin
from django_summernote.admin import SummernoteModelAdmin
from .models                 import Strain, SeedBank, StrainPhoto


# Register your models here.
class  StrainForm(forms.ModelForm):

    class Meta:
        model = Strain
        fields = '__all__'
        widgets = {
            'name': forms.widgets.TextInput(attrs={'style': 'width:90%;'})
        }

class StrainPhotoModelAdmin(admin.ModelAdmin):
    pass

class StrainPhotoInline(admin.StackedInline):
    model = StrainPhoto
    max_num = 5
    extra = 3

class StrainModelAdmin(SummernoteModelAdmin):
    form = StrainForm
    inlines = [StrainPhotoInline,]

admin.site.register(Strain, StrainModelAdmin)
admin.site.register(SeedBank)
