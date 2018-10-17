# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView

from orders.forms import OrderForm

# Create your views here.
class OrderView(FormView):
    template_name = 'order.html'
    form_class = OrderForm
    succes_url = ''
