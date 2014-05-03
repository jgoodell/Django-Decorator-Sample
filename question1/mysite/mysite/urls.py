from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^data/', include('geodata.urls')),
                       url(r'^', include('geodata.urls')),
)
