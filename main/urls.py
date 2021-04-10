# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('staff/list', views.staffs, name="stafflist"),
    path('promotion/list', views.promotions, name="promotionlist"),
    path('department/list', views.departments, name="departmentlist"),
    path('posting/list', views.postings, name="postinglist"),
    path('leave/list', views.leaves, name="leavelist"),
    path('staff/add', views.addstaff, name="addstaff"),
    path('promotion/add', views.addpromotion, name="addpromotion"),
    path('department/add', views.adddepartment, name="adddepartment"),
    path('posting/add', views.addposting, name="addposting"),
    path('leave/add', views.addleave, name="addleave"),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]