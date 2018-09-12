# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Strain, StrainPhoto
import pydash

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class StrainListView(ListView):
    model = Strain

    def get_context_data(self, **kwargs):
        strains = Strain.objects.order_by('name').values('name', 'id')
        kwargs['strains'] = pydash.group_by(strains, lambda strain: strain['name'][0].lower() if strain['name'][0].isalpha() else 'other')
        return super(StrainListView, self).get_context_data(**kwargs)

class StrainDeatailView(DetailView):
    model = Strain

    def get_context_data(self, **kwargs):
        context = super(StrainDeatailView, self).get_context_data(**kwargs)
        context['photos'] = StrainPhoto.objects.filter(strain=self.get_object())
        return context
