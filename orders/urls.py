from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'orders'
urlpatterns = [
    url(r'^$', views.OrderView.as_view(), name='order'),
    url(r'success/$', TemplateView.as_view(template_name='success.html'), name='success'),
]
