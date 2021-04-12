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
    form = PostingForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('postinglist')
    return render(request, 'postings/add.html', {"segment": "addposting", 'form': form})

def addgeopolitical_zone(request):
    form = Geopolitical_ZoneForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('geopolitical_zonelist')
    return render(request, 'geopolitical_zones/add.html',
     {"segment": "addgeopolitical_zone", 'form': form})

def addgrade_level(request):
    form = Grade_LevelForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('grade_levellist')
    return render(request, 'grade_levels/add.html',
     {"segment": "addgrade_level", 'form': form})

def addsalary_structure(request):
    form = Salary_StructureForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('salary_structurelist')
    return render(request, 'salary_structures/add.html',
     {"segment": "addsalary_structure", 'form': form})

def addstate_of_origin(request):
    form = State_Of_OriginForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('state_of_originlist')
    return render(request, 'state_of_origins/add.html',
     {"segment": "addstate_of_origin", 'form': form})

def addleavetype(request):
    form = LeaveTypeForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('leavetypelist')
    return render(request, 'leavetypes/add.html',
     {"segment": "addleavetype", 'form': form})

def addterminaltype(request):
    form = TerminalTypeForm(request.POST or None)
    if request.method == 'POST': 
        if form.is_valid():
            form.save()
            return redirect('terminaltypelist')
    return render(request, 'terminaltypes/add.html',
     {"segment": "addterminaltype", 'form': form})

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
    return render(request, 'postings/postings.html',
     {'page_obj': page_obj, 'segment': "postinglist"})

def geopolitical_zones(request):
    context = {}
    context['segment'] = 'geopolitical_zones'
    geopolitical_zones = Geopolitical_Zone.objects.all()
    paginator = Paginator(geopolitical_zones, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'geopolitical_zones/geopolitical_zones.html',
     {'page_obj': page_obj, 'segment': "geopolitical_zonelist"})

def grade_levels(request):
    context = {}
    context['segment'] = 'grade_levels'
    grade_levels = Grade_Level.objects.all()
    paginator = Paginator(grade_levels, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'grade_levels/grade_levels.html',
     {'page_obj': page_obj, 'segment': "grade_levellist"})

def salary_structures(request):
    context = {}
    context['segment'] = 'salary_structures'
    salary_structures = Salary_Structure.objects.all()
    paginator = Paginator(salary_structures, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'salary_structures/salary_structures.html',
     {'page_obj': page_obj, 'segment': "salary_structurelist"})

def state_of_origins(request):
    context = {}
    context['segment'] = 'state_of_origins'
    state_of_origins = State_Of_Origin.objects.all()
    paginator = Paginator(state_of_origins, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'state_of_origins/state_of_origins.html',
     {'page_obj': page_obj, 'segment': "state_of_originlist"})

def leavetypes(request):
    context = {}
    context['segment'] = 'leavetypes'
    leavetypes = LeaveType.objects.all()
    paginator = Paginator(leavetypes, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'leavetypes/leavetypes.html',
     {'page_obj': page_obj, 'segment': "leavetypelist"})

def terminaltypes(request):
    context = {}
    context['segment'] = 'terminaltypes'
    terminaltypes = TerminalType.objects.all()
    paginator = Paginator(terminaltypes, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # html_template = loader.get_template( 'staffs.html' )
    return render(request, 'terminaltypes/terminaltypes.html',
     {'page_obj': page_obj, 'segment': "terminaltypelist"})