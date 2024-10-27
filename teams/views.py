from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Team
from .forms import TeamAndUserCreationForm
from django.urls import reverse

# Create your views here.
@login_required
def team_dashboard(request):
    # ログインユーザーの所属チームを取得
    if not hasattr(request.user, 'team'):
        return HttpResponseForbidden("あなたはまだチームに所属していません。")
    
    user_team = request.user.team
    return render(request, 'teams/dashboard.html', {'team': user_team})

def create_team_and_user(request):
    if request.method == 'POST':
        form = TeamAndUserCreationForm(request.POST)
        if form.is_valid():
            team, user = form.save()  # チームとユーザーを同時に作成
            return redirect(reverse('login'))  # 成功時のリダイレクト先を設定
    else:
        form = TeamAndUserCreationForm()
    return render(request, 'teams/create_team.html', {'form': form})