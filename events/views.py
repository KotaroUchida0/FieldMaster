from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event

# イベント一覧ページ
@login_required
def event_list(request):
    # ログインユーザーのチームに関連するイベントのみ取得
    user_team_id = request.user.team_id  # ユーザーのチームIDを取得
    events = Event.objects.filter(team_id=user_team_id)  # チームに関連するイベントを取得
    return render(request, 'events/event_list.html', {'events': events})