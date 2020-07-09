# coding=utf-8
from django.conf.urls import url

from rk import views

urlpatterns = [

    url('^create_user/', views.create_user, name='create_user'),
    url('^api_one/(.*?)/(.*?)/$', views.api_one, name='api_one'),
    url('^api_two/(.*?)/(.*?)/$', views.api_two, name='api_two'),

]