# coding=utf-8
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<title>w+)/$', views.post_detail),
]
"""
What’s going on here? – r’^blog/(?P<id>\d+)

r’^blog/
There’s nothing really new in this part of the url pattern. It just means look for a url that begins with “blog/” in the
 text.
(?P<id>\d+)
?P<id> This is the new bit;  It means that Django will take a value that you pass in the url and transfer it to a view
 as a variable called id.
\d+ is a digit (a character in the range 0-9), and + means the digit is allowed to occur 1 or more times. If a character
 other than a digit is passed in, then it will be ignored.
 
http://localhost:8000/blog/2345/ will work
http://localhost:8000/blog/hello/ will fail.
()
The round brackets group the regular expression together
/$
just means the end of the pattern
"""
