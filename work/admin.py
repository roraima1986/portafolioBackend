from django.contrib import admin
from .models import Work

class WorkAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_project', 'is_work', 'is_design', 'is_active', 'created', 'updated']


admin.site.register(Work, WorkAdmin)

