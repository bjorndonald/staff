from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from django import template
from .models import Staff, Promotion

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
    paginator = Paginator(staffs, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'staffs/staffs.html', {'page_obj': page_obj})

def promotions(request):
    context = {}
    context['segment'] = 'promotions'
    promotions = Promotion.objects.all()
    paginator = Paginator(promotions, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'promotions/promotions.html', {'page_obj': page_obj})