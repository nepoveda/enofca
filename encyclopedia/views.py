# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Strain, StrainPhoto, History, HISTORY_CHOICES
import pydash

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class StrainListView(ListView):
    model = Strain

    def get_context_data(self, **kwargs):
        strains = Strain.objects.order_by('name').values('name', 'webId')
        kwargs['strains'] = pydash.group_by(strains, lambda strain: strain['name'][0].lower() if strain['name'][0].isalpha() else '#')
        return super(StrainListView, self).get_context_data(**kwargs)

class StrainDeatailView(DetailView):
    model = Strain
    slug_field = "webId"
    slug_url_kwarg = "webId"
    query_pk_and_slug = True

    def get_context_data(self, **kwargs):
        context = super(StrainDeatailView, self).get_context_data(**kwargs)
        context['photos'] = StrainPhoto.objects.filter(strain=self.get_object())
        return context

class HistoryListView(ListView):
    model = History

    def get_context_data(self, **kwargs):
        historys = History.objects.order_by('standing')
        kwargs['historys'] = pydash.group_by(historys, lambda history: history.get_period_display())
        return super(HistoryListView, self).get_context_data(**kwargs)
