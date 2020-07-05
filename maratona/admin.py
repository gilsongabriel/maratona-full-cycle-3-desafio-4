from django.contrib import admin

from maratona.models import Class

class ClassAdmin(admin.ModelAdmin):
    list_display = ['description', 'tutor', 'date']
    list_filter = ['description', 'tutor', 'date']
    search_fields = ['description']

admin.site.register(Class, ClassAdmin)