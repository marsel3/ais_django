from django.contrib import admin
from .models import Achievement


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description', 'is_favorite')
    list_display_links = ('title', 'date', 'description')
    search_fields = ('title', 'date', 'description', 'is_favorite')



admin.site.register(Achievement, AchievementAdmin)