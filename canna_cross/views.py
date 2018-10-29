# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView

from django.shortcuts import render

from canna_cross.models import Company
import pydash

# Create your views here.
def company(request, kind=""):
    filter_kwargs={kind: True}
    companys = Company.objects.filter(**filter_kwargs)
    companys = pydash.group_by(companys, lambda company: company.get_continent_display())
    return render(request, 'canna_cross/company_list.html', {'companys': companys})

