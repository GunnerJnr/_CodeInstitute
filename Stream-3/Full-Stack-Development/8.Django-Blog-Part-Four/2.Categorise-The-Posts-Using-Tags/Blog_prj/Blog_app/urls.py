# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/(?P<slug>[-\w]+)$', views.post_detail, name='post_detail'),
]
