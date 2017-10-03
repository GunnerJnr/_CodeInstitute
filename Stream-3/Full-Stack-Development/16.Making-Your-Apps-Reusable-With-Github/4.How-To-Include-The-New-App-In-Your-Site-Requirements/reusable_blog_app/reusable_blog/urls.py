# coding=utf-8
from django.conf.urls import url
import views
from .views import redirect_root

urlpatterns = [
    url(r'^$', redirect_root, name='home'),
    url(r'^blog/$', views.post_list, name='post-list'),
    url(r'^blog/(?P<slug>[-\w]+)$', views.post_detail, name='post-detail'),
    url(r'^blog/top-five/$', views.display_top_five_posts, name='top-five'),
    url(r'^blog/post/new/$', views.new_post, name='new_post'),
    url(r'^blog/(?P<slug>[-\w]+)/edit-post$', views.edit_post, name='edit-post'),
]
