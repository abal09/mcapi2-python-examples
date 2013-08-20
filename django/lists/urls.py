from django.conf.urls import patterns, url

from lists import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<list_id>\w+)/$', views.view, name='view'),
                       url(r'^(?P<list_id>\w+)/subscribe/$', views.subscribe, name='view')
)