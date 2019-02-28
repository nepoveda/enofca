# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ['status']

