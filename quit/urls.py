from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.something_list, name='something_list'),
    url(r'^thing/(?P<pk>\d+)/$', views.thing_detail, name='thing_detail'),
    url(r'^thing/new/$', views.thing_new, name='thing_new'),
    url(r'^thing/(?P<pk>\d+)/edit/$', views.thing_edit, name='thing_edit'),
    url(r'^signup/$', views.signup, name='signup'),
]