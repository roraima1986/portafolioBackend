from django.contrib import admin
from .models import About


class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_published', 'created', 'updated']

admin.site.register(About, AboutAdmin)


