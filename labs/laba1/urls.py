from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='achievement_list'),
    path('achievement/<int:pk>', views.AchievementDetail.as_view(), name='detail_achievement'),
    path('add_edit_delete/', views.add_edit_delete_achievement, name='add_edit_delete_achievement'),
    path('achievement/<int:achievement_id>/add_comment/', views.add_comment, name='add_comment'),
    path('achievement/<int:achievement_id>/like', views.like_achievement, name='like_achievement'),
]