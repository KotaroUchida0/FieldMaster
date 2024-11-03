from django.urls import path
from . import views
from stats import views as stats_views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('<int:match_id>/', views.match_detail, name='match_detail'),
    path('<int:match_id>/update/', views.update_match, name='update_match'),
    path('<int:match_id>/create_hitter_stats/', stats_views.create_hitter_stats, name='create_hitter_stats'),
    path('<int:match_id>/create_pitcher_stats/', stats_views.create_pitcher_stats, name='create_pitcher_stats'),
]