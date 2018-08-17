# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import Strain

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

class StrainListView(ListView):
    model = Strain

    # def get_context_data(self, **kwargs):
    #     kwargs['seeds'] = Strain.objects.order_by('name')
    #     return super(IndexView, self).get_context_data(**kwargs)

class StrainDeatailView(DetailView):
    model = Strain

