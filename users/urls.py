from django.urls import path
from .views import EmailLoginView
from . import views

urlpatterns = [
    path('login/', EmailLoginView.as_view(), name='login'),
    path('add/', views.create_user, name='create_user'),
    path('members/', views.member_list, name='member_list'),
    path('<int:user_id>/', views.member_detail, name='member_detail')
]
