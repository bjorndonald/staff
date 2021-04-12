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
    path('geopolitical_zone/list', views.geopolitical_zones, name="geopolitical_zonelist"),
    path('grade_level/list', views.grade_levels, name="grade_levellist"),
    path('salary_structure/list', views.salary_structures, name="salary_structurelist"),
    path('state_of_origin/list', views.state_of_origins, name="state_of_originlist"),
    path('leavetype/list', views.leavetypes, name="leavetypelist"),
    path('terminaltype/list', views.terminaltypes, name="terminaltypelist"),

    path('staff/add', views.addstaff, name="addstaff"),
    path('promotion/add', views.addpromotion, name="addpromotion"),
    path('department/add', views.adddepartment, name="adddepartment"),
    path('posting/add', views.addposting, name="addposting"),
    path('leave/add', views.addleave, name="addleave"),
    path('geopolitical_zone/add', views.addgeopolitical_zone, name="addgeopolitical_zone"),
    path('grade_level/add', views.addgrade_level, name="addgrade_level"),
    path('salary_structure/add', views.addsalary_structure, name="addsalary_structure"),
    path('state_of_origin/add', views.addstate_of_origin, name="addstate_of_origin"),
    path('leavetype/add', views.addleavetype, name="addleavetype"),
    path('terminaltype/add', views.addterminaltype, name="addterminaltype"),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]