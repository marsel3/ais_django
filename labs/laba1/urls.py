from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='achievement_list'),
    path('achievement/<int:pk>', views.AchievementDetail.as_view(), name='detail_achievement'),
    path('add_edit_delete/', views.add_edit_delete_achievement, name='add_edit_delete_achievement'),
]