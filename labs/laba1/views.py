from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Achievement, Comment, Like
from django.views.generic import ListView, DetailView
from .forms import AchievementForm, CommentForm
from django.http import Http404
from django.db.models import Count


def index(request):
    sort_by = request.GET.get('sort_by', 'date')
    sort_order = request.GET.get('sort_order', 'sort')
    sort_order = 'asc' if not sort_order else 'asc' if sort_order == 'desc' else 'desc'
    type = '-' if sort_order == 'asc' else ''

    if sort_by not in ['date', 'title', 'likes']:
        sort_by = 'date'

    if sort_by == 'date':
        achievements = Achievement.objects.all().order_by(f'{type}date')
    elif sort_by == 'title':
        achievements = Achievement.objects.all().order_by(f'{type}title')
    else:
        achievements = Achievement.objects.annotate(like_count=Count('like')).order_by(f'{type}like_count')

    context = {
        'achievements': achievements,
        'sort_by': sort_by,
        'sort': sort_order,
    }

    return render(request, 'laba1/achievement_list.html', context)


class AchievementDetail(DetailView):
    model = Achievement
    template_name = 'laba1/achievement.html'
    context_object_name = 'achievement'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        achievement = self.get_object()
        comments = Comment.objects.filter(achievement=achievement)

        likes = Like.objects.filter(achievement=achievement, liked=True).count()
        dislikes = Like.objects.filter(achievement=achievement, liked=False).count()

        user = self.request.user
        liked_by_user = False
        disliked_by_user = False

        if user.is_authenticated:
            liked_by_user = Like.objects.filter(achievement=achievement, user=user, liked=True).exists()
            disliked_by_user = Like.objects.filter(achievement=achievement, user=user, liked=False).exists()

        context['comments'] = comments
        context['likes'] = likes
        context['dislikes'] = dislikes
        context['liked_by_user'] = liked_by_user
        context['disliked_by_user'] = disliked_by_user
        return context


def add_edit_delete_achievement(request):
    if request.user.is_authenticated and request.user.is_staff:
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
    else:
        return redirect('/accounts/login')


def add_comment(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.achievement = achievement
                comment.user = request.user
                comment.save()
                return redirect(f'/achievement/{achievement_id}', achievement_id=achievement.id)
        else:
            return redirect('/accounts/login')

    return redirect('detail_achievement', pk=achievement.id)


def like_achievement(request, achievement_id):
    achievement = get_object_or_404(Achievement, pk=achievement_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            like, created = Like.objects.get_or_create(achievement=achievement, user=request.user)

            if 'like' in request.POST:
                like.liked = True
                like.save()
            elif 'dislike' in request.POST:
                like.liked = False
                like.save()
            elif 'unlike' in request.POST:
                like.delete()
            elif 'undislike' in request.POST:
                like.delete()
        else:
            return redirect('/accounts/login')

    return redirect('detail_achievement', pk=achievement.id)