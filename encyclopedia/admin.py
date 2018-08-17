# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django                  import forms
from django.contrib          import admin
from django_summernote.admin import SummernoteModelAdmin
from .models                 import Strain


# Register your models here.
class  StrainForm(forms.ModelForm):

    class Meta:
        model = Strain
        fields = '__all__'
        widgets = {
            'name': forms.widgets.TextInput(attrs={'style': 'width:90%;'})
        }

class StrainModelAdmin(SummernoteModelAdmin):
    form = StrainForm

admin.site.register(Strain, StrainModelAdmin)
