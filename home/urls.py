#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/10 14:21
# @Author  : mrwuzs
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from .views import home

urlpatterns = [
    path('',home,name='home'),
]