"""iti URL Configuration

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
from django.conf.urls import url , include
from django.contrib import admin

from django.contrib.auth import urls

from Countries import views

urlpatterns = [
    url(r'^home/$', views.displayHome),
    url(r'^(?P<country_name>[A-Za-z , A-Za-z]+)/$' , views.showCountry , name='country'),
    #url(r'^home/city/(?P<city_name>[A-Za-z-A-Za-z]+)/$', views.showCity, name='city'),
    url(r'^(?P<country_name>[A-Za-z , A-Za-z]+)/(?P<city_name>[A-Za-z \- A-Za-z]+)/$', views.showCity, name='city'),
    url(r'^(?P<country_name>[A-Za-z , A-Za-z]+)/(?P<city_name>[A-Za-z \- A-Za-z]+)/post/(?P<exper_ID>[0-9]+)/$', views.addComment, name='comment'),
    # url(r'^(?P<country_name>[A-Za-z , A-Za-z]+)/(?P<city_name>[A-Za-z \- A-Za-z]+)/comment/(?P<exper_ID>[0-9]+)/$', views.addComment, name='comment'),
]