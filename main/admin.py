from django.contrib import admin
from .models import *

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