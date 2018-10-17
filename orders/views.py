# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy, reverse

from orders.forms import OrderForm
from orders.models import Order

# Create your views here.
class OrderView(FormView):
    template_name = 'order.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:success')
