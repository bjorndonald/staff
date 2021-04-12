from django.contrib import admin
from .models import *

from django.contrib.auth.models import User, Group

if not Group.objects.filter(name="Hod"):
	hod = Group()
	hod.name = "HOD"
	hod.save()
elif not Group.objects.filter(name="Staff"):
	staff = Group()
	staff.name = "Staff"
	staff.save()
# elif not Group.objects.filter(name="Receptionist"):
# 	receptionist = Group()
# 	receptionist.name = "Receptionist"
# 	receptionist.save()
# elif not Group.objects.filter(name="Admin"):
# 	admin = Group()
# 	admin.name = "Admin"
# 	admin.save()
# elif not Group.objects.filter(name="ChiefMedical"):
# 	chief = Group()
# 	chief.name = "ChiefMedical"
# 	chief.save()

# adminobj = User.objects.get(username="admin")
# if not adminobj.groups.all():
# 	admin_group = Group.objects.get(name='Admin')
# 	adminobj.groups.add(admin_group)


class StaffAdmin(admin.ModelAdmin):
	list_display = ('staff_name','rank')
	list_display_links =('staff_name',)

class State_Of_OriginAdmin(admin.ModelAdmin):
	list_display = ('state_name',)
	list_display_links =('state_name',)

class StepAdmin(admin.ModelAdmin):
	list_display = ('step',)
	list_display_links =('step',)

class Grade_LevelAdmin(admin.ModelAdmin):
	list_display = ('grade_level_name',)
	list_display_links =('grade_level_name',)

class RankAdmin(admin.ModelAdmin):
	list_display = ('rank',)
	list_display_links =('rank',)

class Geopolitical_ZoneAdmin(admin.ModelAdmin):
	list_display = ('geopolitical_zone',)
	list_display_links =('geopolitical_zone',)

# Register your models here.
admin.site.register(Staff,StaffAdmin)
admin.site.register(State_Of_Origin, State_Of_OriginAdmin)
admin.site.register(Step, StepAdmin)
admin.site.register(Grade_Level, Grade_LevelAdmin)
admin.site.register(Rank, RankAdmin)
admin.site.register(Geopolitical_Zone, Geopolitical_ZoneAdmin)