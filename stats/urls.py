from django.urls import path
from . import views

urlpatterns = [
    path('total_stats/', views.total_stats, name='total_stats'),
    path('titles/', views.title_page, name='title_page'),
]