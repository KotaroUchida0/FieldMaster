from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.team_dashboard, name='team_dashboard'),
]
