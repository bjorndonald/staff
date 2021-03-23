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
    path('promotions/list', views.promotions, name="promotionlist")
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]