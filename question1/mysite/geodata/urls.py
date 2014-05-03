from django.conf.urls import patterns, url

from geodata import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^data/(?P<state>\w+)$', views.data, name='data'),
                       )
