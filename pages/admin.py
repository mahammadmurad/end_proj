from django.contrib import admin
from .models import Project, Achievement

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('message', )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('message', )