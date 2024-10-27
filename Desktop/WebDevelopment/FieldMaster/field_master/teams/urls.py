from django.urls import path
from . import views

urlpatterns = [
    path('', views.team_dashboard, name='team_dashboard'),
    path('create/', views.create_team_and_user, name='create_team_and_user'),
]
