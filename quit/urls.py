from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.something_list, name='something_list'),
    url(r'^thing/(?P<pk>\d+)/$', views.thing_detail, name='thing_detail'),
]