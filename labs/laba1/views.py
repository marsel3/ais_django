from django.shortcuts import render
from django.http import HttpResponse
from .models import Achievement
from django.views.generic import ListView, DetailView


def index(request):
    achievements = Achievement.objects.order_by('date')
    data = {"achievements": achievements}

    return render(request, 'laba1/achievement_list.html', data)


class AchievementDetail(DetailView):
    model = Achievement
    template_name = 'laba1/achievement.html'
    context_object_name = 'achievement'


class AchievementList(ListView):
    model = Achievement
    template_name = 'laba1/achievement_list.html'
    context_object_name = 'achievements'
    ordering = ['date']

