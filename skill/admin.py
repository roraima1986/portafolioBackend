from django.contrib import admin
from .models import Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'updated']


admin.site.register(Skill, SkillAdmin)
