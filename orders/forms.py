# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        exclude = ['status', 'client', 'address']

    def clean_agree(self):
        agree = self.cleaned_data['agree']
        if not agree:
            raise ValidationError('This field is required')

        return agree

