from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

# イベント一覧ページ
@login_required
def event_list(request):
    # ログインユーザーのチームに関連するイベントのみ取得
    user_team_id = request.user.team_id  # ユーザーのチームIDを取得
    events = Event.objects.filter(team_id=user_team_id)  # チームに関連するイベントを取得
    return render(request, 'events/event_list.html', {'events': events})

# イベント作成ページ
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            # ログインユーザーのチームを設定
            event.team_id = request.user.team  # Teamインスタンスを割り当て
            event.save()
            return redirect(reverse('events'))  # イベント一覧ページにリダイレクト
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})