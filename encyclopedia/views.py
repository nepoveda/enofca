# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Seed

# Create your views here.
class IndexView(ListView):
    model = Seed
    template_name = 'index.html'

class SeedDeatailView(DetailView):
    model = Seed
    template_name = 'seed_detail.html'

