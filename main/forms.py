from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.password_validation import MinimumLengthValidator, NumericPasswordValidator
from django.core.validators import validate_email
from django.forms.widgets import HiddenInput

class LeaveForm(forms.ModelForm):
    status = forms.BooleanField(required=True, label="Status")
    date = forms.DateField(label="Leave Date", widget=forms.DateInput(attrs={'type':'date'}))
    message = forms.CharField( label="Message", widget=forms.Textarea)

    class Meta:
        model = Leave
        fields = ['status', 'date', 'message']

    def __init__(self, *args, **kwargs):
        super(LeaveForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class StaffForm(forms.ModelForm):
    staff_name = forms.CharField( label="Staff Name", widget=forms.TextInput(attrs={'class': "form-control form-control-alternative", 'placeholder': 'Paul Ekanem'}))
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type':'date'}))
    date_of_first_appointment = forms.DateField(label="Date of First Appointment", widget=forms.DateInput(attrs={'type':'date'}))
    phone_no = forms.CharField(label="Phone Number")
    file_no = forms.CharField(label="File Number")
    confirmation_date = forms.DateField(label="Confirmation Date", widget=forms.DateInput(attrs={'type':'date'}))
    address = forms.CharField(label="Address", widget=forms.Textarea)
    location = forms.CharField(label="Location", widget=forms.Textarea)
    state= forms.ModelChoiceField(queryset=State_Of_Origin.objects.all())
    step= forms.ModelChoiceField(queryset=Step.objects.all())
    grade_level= forms.ModelChoiceField(queryset=Grade_Level.objects.all())
    rank= forms.ModelChoiceField(queryset=Rank.objects.all())
    geopolitical_zone = forms.ModelChoiceField(queryset=Geopolitical_Zone.objects.all())

    class Meta:
        model = Staff
        fields = ['staff_name','date_of_birth', 'date_of_first_appointment',
        'phone_no', 'file_no', 'confirmation_date', 'address', 'location', 'state',
        'step', 'grade_level', 'rank', 'geopolitical_zone']

    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PostingForm(forms.ModelForm):
    staff = forms.ModelChoiceField(queryset=Staff.objects.all())
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    start_date = forms.DateField(label="Start Date", widget=forms.DateInput(attrs={'type':'date'}))
    end_date = forms.DateField(label="End Date", widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = Posting
        fields = ['staff', 'department', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super(PostingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class QualificationForm(forms.ModelForm):
    qualification_name = forms.CharField(label="Qualification Name")
    qualification_date = forms.DateField(label="Qualification Date", widget=forms.DateInput(attrs={'type':'date'}))
    staff = forms.ModelChoiceField(queryset=Staff.objects.all())

    class Meta:
        model = Qualification
        fields = ['staff', 'qualification_name', 'qualification_date']

    def __init__(self, *args, **kwargs):
        super(QualificationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Geopolitical_ZoneForm(forms.ModelForm):
    geopolitical_zone = forms.CharField(label="Geopolitical Zone")

    class Meta:
        model = Geopolitical_Zone
        fields = ['geopolitical_zone']

    def __init__(self, *args, **kwargs):
        super(Geopolitical_ZoneForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Grade_LevelForm(forms.ModelForm):
    grade_level_name = forms.CharField(label="Geopolitical Zone")

    class Meta:
        model = Grade_Level
        fields = ['grade_level_name']

    def __init__(self, *args, **kwargs):
        super(Grade_LevelForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class Salary_StructureForm(forms.ModelForm):
    salary_structure_name = forms.CharField(label="Salary Structure")

    class Meta:
        model = Salary_Structure
        fields = ['salary_structure_name']

    def __init__(self, *args, **kwargs):
        super(Salary_StructureForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class State_Of_OriginForm(forms.ModelForm):
    state_name = forms.CharField(label="State of Origin")

    class Meta:
        model = State_Of_Origin
        fields = ['state_name']

    def __init__(self, *args, **kwargs):
        super(State_Of_OriginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class LeaveTypeForm(forms.ModelForm):
    name = forms.CharField(label="Leave Type")

    class Meta:
        model = LeaveType
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(LeaveTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TerminalTypeForm(forms.ModelForm):
    name = forms.CharField(label="Terminal Type")

    class Meta:
        model = TerminalType
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(TerminalTypeForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class DepartmentForm(forms.ModelForm):
    name = forms.CharField(label="Department Name")

    class Meta:
        model = Department
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class PromotionForm(forms.ModelForm):
    promotion_date = forms.DateField(label="Promotion Date", widget=forms.DateInput(attrs={'type':'date'}))
    grade_level = forms.ModelChoiceField(queryset=Grade_Level.objects.all())
    staff = forms.ModelChoiceField(queryset=Staff.objects.all())
    step = forms.ModelChoiceField(queryset=Step.objects.all())

    class Meta:
        model = Promotion
        fields = ['staff', 'grade_level', 'step', 'promotion_date']

    def __init__(self, *args, **kwargs):
        super(PromotionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'