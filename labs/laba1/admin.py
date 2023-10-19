from django.contrib import admin
from .models import Achievement, Comment, Like


class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')
    list_display_links = ('title', 'date', 'description')
    search_fields = ('title', 'date', 'description')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'user', 'text', 'timestamp')
    list_display_links = ('achievement', 'user', 'text', 'timestamp')
    search_fields = ('achievement', 'user', 'text', 'timestamp')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('achievement', 'user', 'liked')
    list_display_links = ('achievement', 'user', 'liked')
    search_fields = ('achievement', 'user', 'liked')


admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Achievement, AchievementAdmin)