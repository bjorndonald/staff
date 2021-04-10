from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.core.paginator import Paginator
from django import template
from .models import *
from .forms import *

# Create your views here.
def index(request):
    
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return render(request, 'index.html', {"segment": "index"})

def addstaff(request):
    form = StaffForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('stafflist')
    return render(request, 'staffs/add.html', {"segment": "addstaff", 'form': form})

def addleave(request):
    form = LeaveForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid(): 
            form.save()
            return redirect('leavelist')
    return render(request, 'leaves/add.html', {"segment": "addleave", 'form': form})

def addpromotion(request):
    form = PromotionForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('promotionlist')
    return render(request, 'promotions/add.html', {"segment": "addpromotion", 'form': form})

def adddepartment(request):
    context = {}
    return render(request, 'departments/add.html', {"segment": "adddepartment"})

def addposting(request):
    form = PromotionForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('postinglist')
    return render(request, 'postings/add.html', {"segment": "addposting", 'form': form})

def staffs(request):
    context = {}
    context['segment'] = 'staffs'
    staffs = Staff.objects.all()
    paginator = Paginator(staffs, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'staffs/staffs.html', {'page_obj': page_obj, 'segment': "stafflist"})

def promotions(request):
    context = {}
    context['segment'] = 'promotions'
    promotions = Promotion.objects.all()
    paginator = Paginator(promotions, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'promotions/promotions.html', {'page_obj': page_obj, 'segment': "promotionlist"})

def leaves(request):
    context = {}
    context['segment'] = 'leaves'
    leaves = Leave.objects.all()
    paginator = Paginator(leaves, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'leaves/leaves.html', {'page_obj': page_obj, 'segment': "leavelist"})

def departments(request):
    context = {}
    context['segment'] = 'departments'
    departments = Department.objects.all()
    paginator = Paginator(departments, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'departments/departments.html',
     {'page_obj': page_obj, 'segment': "departmentlist"})

def postings(request):
    context = {}
    context['segment'] = 'postings'
    postings = Posting.objects.all()
    paginator = Paginator(postings, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'postings/postings.html', {'page_obj': page_obj, 'segment': "postinglist"})