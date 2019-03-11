# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy, reverse
from django.views.generic.base import View, TemplateResponseMixin
from django.views.generic.edit import FormMixin, ProcessFormView
from django.http import HttpResponseRedirect
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from orders.forms import OrderForm
from orders.models import Order
from clients.forms import AddressForm, ClientForm


class MultipleFormsMixin(FormMixin):
    """
    A mixin that provides a way to show and handle several forms in a
    request.
    """
    form_classes = {} # set the form classes as a mapping

    def get_form_classes(self):
        return self.form_classes

    def get_forms(self, form_classes):
        return dict([(key, klass(**self.get_form_kwargs())) for key, klass in form_classes.items()])

    def forms_valid(self, forms):
        return super(MultipleFormsMixin, self).form_valid(forms)

    def forms_invalid(self, forms):
        return self.render_to_response(self.get_context_data(forms=forms))


class ProcessMultipleFormsView(ProcessFormView):
    """
    A mixin that processes multiple forms on POST. Every form must be
    valid.
    """
    def get(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        return self.render_to_response(self.get_context_data(forms=forms))

    def post(self, request, *args, **kwargs):
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        if all([form.is_valid() for form in
            forms.values()]):
            return self.forms_valid(forms)
        else:
            return self.forms_invalid(forms)


class BaseMultipleFormsView(MultipleFormsMixin, ProcessMultipleFormsView):
    """
    A base view for displaying several forms.
    """

class MultipleFormsView(TemplateResponseMixin, BaseMultipleFormsView):
    """
    A view for displaing several forms, and rendering a template response.
    """
def send_order_email(order_id, to_email):
    subject = 'Order form ENOFCA ({})'.format(order_id)
    html_template = render_to_string('order_mail.html', {'order': order_id})
    plain_message = strip_tags(html_template)
    from_email = 'eshop@enofca.com'
    mail.send_mail(subject, plain_message, from_email, [to_email], html_message=html_template)

def send_info_email(order, client, address):
    subject = 'Order form ENOFCA ({})'.format(order.id)
    html_template = render_to_string('order_info_mail.html', {'order': order,
                                                         'client': client,
                                                         'address': address})
    plain_message = strip_tags(html_template)
    from_email = 'eshop@enofca.com'
    mail.send_mail(subject, plain_message, from_email, ['info@enofca.com'], html_message=html_template)

class OrderView(MultipleFormsView):
    template_name = 'order.html'
    success_url = reverse_lazy('orders:success')
    form_class=OrderForm
    form_classes = {
        'orderForm': OrderForm,
        'clientForm': ClientForm,
        'addressForm': AddressForm,
    }

    def post(self, request, *args, **kwargs):
        super(OrderView, self).post(request, *args, **kwargs)
        form_classes = self.get_form_classes()
        forms = self.get_forms(form_classes)
        client_form = forms.get('clientForm')
        address_form = forms.get('addressForm')
        order_form = forms.get('orderForm')
        if client_form.is_valid() and address_form.is_valid() and order_form.is_valid():
            client = client_form.save()
            client.save()
            address = address_form.save()
            address.save()
            order = Order.objects.create(
                quantity = order_form.cleaned_data['quantity'],
                agree = order_form.cleaned_data['agree'],
                client = client,
                address = address
            )
            order.save()
            send_order_email(order.id, client.email)
            send_info_email(order, client, address)
            return HttpResponseRedirect(reverse('orders:success'))
        return render(request, self.template_name, {
            'forms': forms
        })

