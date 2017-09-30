# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r"^$", views.post_list, name="post-list"),
    url(r"^/$", views.post_list, name="post-list"),
    url(r'^(?P<slug>[-\w]+)$', views.post_detail, name='post-detail'),
    url(r'^top-five/$', views.display_top_five_posts, name='top-five'),
    url(r'^post/new/$', views.new_post, name='new_post'),
    url(r'^(?P<slug>[-\w]+)/edit-post$', views.edit_post, name='edit-post'),
]
