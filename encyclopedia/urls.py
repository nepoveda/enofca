from django.conf.urls import url

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'strains/$', views.StrainListView.as_view(), name="strain-list"),
    url(r'strains/(?P<pk>[0-9]+)/$', views.StrainDeatailView.as_view(), name="strain"),
]
