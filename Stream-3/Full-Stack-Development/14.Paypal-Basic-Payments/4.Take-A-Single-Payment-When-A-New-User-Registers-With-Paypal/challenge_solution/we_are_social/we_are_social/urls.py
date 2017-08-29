"""we_are_social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.flatpages import views
from paypal.standard.ipn import urls as paypal_urls
from paypal_store import views as paypal_views
from accounts import views as accounts_views
from hello import views as hello_views
from products import views as product_views


urlpatterns = [
    # admin backend url
    url(r'^admin/', admin.site.urls),
    # hello urls
    url(r'^$', hello_views.get_index, name='index'),
    # accounts urls
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^about/$', views.flatpage, {'url': '/pages/about/'}, name='about'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', accounts_views.subscriptions_webhook, name='subscriptions_webhook'),
    # paypal urls
    url(r'^a-very-hard-to-guess-url/', include(paypal_urls)),
    url(r'^paypal-return/', paypal_views.paypal_return),
    url(r'^paypal-cancel/', paypal_views.paypal_cancel),
    # products urls
    url(r'^products/$', product_views.all_products),
]
