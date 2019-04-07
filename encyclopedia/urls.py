from django.conf.urls import url

from . import views

app_name = 'encyclopedia'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'strains/$', views.StrainListView.as_view(), name="strain-list"),
    url(r'history/$', views.HistoryListView.as_view(), name='history'),
    url(r'cups/$', views.CupListView.as_view(), name='cups'),
    url(r'strains/(?P<webId>[0-9]+)/$', views.StrainDeatailView.as_view(), name="strain"),
    url(r'history/(?P<pk>[0-9]+)/$', views.HistoryDetailView.as_view(), name="history_detail")
]

