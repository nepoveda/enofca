# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django                  import forms
from django.contrib          import admin
from django_summernote.admin import SummernoteModelAdmin
from .models                 import Seed


# Register your models here.
class  SeedForm(forms.ModelForm):

    class Meta:
        model = Seed
        fields = '__all__'
        widgets = {
            'name': forms.widgets.TextInput(attrs={'style': 'width:90%;'})
        }

class SeedModelAdmin(SummernoteModelAdmin):
    form = SeedForm

admin.site.register(Seed, SeedModelAdmin)
