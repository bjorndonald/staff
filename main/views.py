from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Staff

# Create your views here.
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return render(request, 'index.html', {"segment": "index"})

def staffs(request):
    context = {}
    context['segment'] = 'staffs'
    staffs = Staff.objects.all()
    html_template = loader.get_template( 'staffs.html' )
    return render(request, 'staffs.html', {"staffs": staffs})