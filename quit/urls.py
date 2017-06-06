from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.something_list, name='something_list'),
]