from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def team_dashboard(request):
    # ログインユーザーの所属チームを取得
    if not hasattr(request.user, 'team'):
        return HttpResponseForbidden("あなたはまだチームに所属していません。")
    
    user_team = request.user.team
    return render(request, 'teams/dashboard.html', {'team': user_team})