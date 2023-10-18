from django.shortcuts import render
from django.http import HttpResponse
from .models import Achievement
from django.views.generic import ListView, DetailView


def index(request):
    sort_by = request.GET.get('sort_by', 'date')
    if sort_by not in ['date', 'title', 'is_favorite']:
        sort_by = 'date'

    if sort_by == 'date':
        achievements = Achievement.objects.all().order_by('date')
    elif sort_by == 'title':
        achievements = Achievement.objects.all().order_by('title')
    else:
        achievements = Achievement.objects.all().order_by('-is_favorite', 'date')

    context = {
        'achievements': achievements,
        'sort_by': sort_by,
    }

    return render(request, 'laba1/achievement_list.html', context)

    """achievements = Achievement.objects.order_by('date')
    data = {"achievements": achievements}

    return render(request, 'laba1/achievement_list.html', data)"""


class AchievementDetail(DetailView):
    model = Achievement
    template_name = 'laba1/achievement.html'
    context_object_name = 'achievement'


class AchievementList(ListView):
    model = Achievement
    template_name = 'laba1/achievement_list.html'
    context_object_name = 'achievements'
    ordering = ['date']

