from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^beer/$', views.all_beers, name='all_beers'),
    url(r'^beer/(?P<name>[\w\-]+)/$', views.beer, name='beer'),
    url(r'^(?P<url>http.+)/$', views.menu, name='menu')
)
