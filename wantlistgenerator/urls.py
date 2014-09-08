from django.conf.urls import patterns, url

from wantlistgenerator import views

urlpatterns = patterns('',
                       url(r'^$', views.riassunto, name='riassunto'),
                       )
