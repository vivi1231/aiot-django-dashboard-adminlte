# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from django.conf.urls import url
from app import views


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route 
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls")),             # UI Kits Html files

    url(r'^listone/$', views.listone),
    url(r'^listall/$', views.listall),

    url(r'^insert/$', views.insert),   #新增資料
    url(r'^modify/$', views.modify),   #修改資料
    url(r'^delete/$', views.delete),   #刪除資料


]
