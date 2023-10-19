from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Achievement
from django.views.generic import ListView, DetailView
from .forms import AchievementForm
from django.http import Http404


def index(request):
    sort_by = request.GET.get('sort_by', 'date')
    if sort_by not in ['date', 'title']:
        sort_by = 'date'

    if sort_by == 'date':
        achievements = Achievement.objects.all().order_by('date')
    else:
        achievements = Achievement.objects.all().order_by('title')

    context = {
        'achievements': achievements,
        'sort_by': sort_by,
    }

    return render(request, 'laba1/achievement_list.html', context)


class AchievementDetail(DetailView):
    model = Achievement
    template_name = 'laba1/achievement.html'
    context_object_name = 'achievement'


def add_edit_delete_achievement(request):
    achievement_id = request.GET.get('achievement_id', None)
    if achievement_id:
        achievement = get_object_or_404(Achievement, pk=achievement_id)
    else:
        achievement = None

    if request.method == 'POST':
        if 'delete' in request.POST and achievement:
            achievement.delete()
            return redirect('add_edit_delete_achievement')
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect('add_edit_delete_achievement')
    else:
        form = AchievementForm(instance=achievement)

    achievements = Achievement.objects.all()
    context = {
        'form': form,
        'achievements': achievements,
        'achievement': achievement,
    }

    return render(request, 'laba1/add_edit_delete_achievement.html', context)
