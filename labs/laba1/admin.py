from django.contrib import admin
from .models import Achievement


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')
    list_display_links = ('title', 'date', 'description')
    search_fields = ('title', 'date', 'description')


admin.site.register(Achievement, AchievementAdmin)