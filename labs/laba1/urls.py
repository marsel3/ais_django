from django.urls import path
from . import views


urlpatterns = [
    path('', views.AchievementList.as_view(), name='achievements'),
    path('achievement/<int:pk>', views.AchievementDetail.as_view(), name='detail_achievement'),
]
