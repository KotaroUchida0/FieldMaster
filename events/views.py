from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Event, Attendance
from .forms import EventForm, AttendanceForm


# イベント一覧ページ
@login_required
def event_list(request):
    # ログインユーザーのチームに関連するイベントのみ取得
    user_team_id = request.user.team_id
    events = Event.objects.filter(team_id=user_team_id)

    # ログインユーザーの各イベントごとの出欠ステータスを取得
    user_attendance = Attendance.objects.filter(user_id=request.user.id, event_id__in=events).select_related('event_id')
    user_attendance_status = {att.event_id.id: att.status for att in user_attendance}

    return render(request, 'events/event_list.html', {
        'events': events,
        'user_attendance_status': user_attendance_status,
    })

# イベント作成ページ
@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.team_id = request.user.team  # Teamインスタンスを割り当て
            event.save()
            return redirect(reverse('events'))  # イベント一覧ページにリダイレクト
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

#イベント詳細ページ
@login_required
def event_detail(request, event_id):
    # イベントの詳細情報を取得
    event = get_object_or_404(Event, id=event_id, team_id=request.user.team)
    
    # チームの参加状況（出欠データ）を取得
    attendance_list = Attendance.objects.filter(event_id=event_id).select_related('user_id')
    
    # 出席、欠席、未定の人数を集計
    attendance_counts = attendance_list.values('status').annotate(count=Count('status'))
    attendance_summary = {
        'present': next((item['count'] for item in attendance_counts if item['status'] == 'present'), 0),
        'absent': next((item['count'] for item in attendance_counts if item['status'] == 'absent'), 0),
        'undecided': next((item['count'] for item in attendance_counts if item['status'] == 'undecided'), 0),
    }

    return render(request, 'events/event_detail.html', {
        'event': event,
        'attendance_list': attendance_list,
        'attendance_summary': attendance_summary,
    })

#イベント削除機能
@login_required
def delete_event(request, event_id):
    # イベントを取得（存在しない場合は404エラーを返す）
    event = get_object_or_404(Event, id=event_id, team_id=request.user.team)
    
    if request.method == "POST":
        event.delete()  # イベントを削除
        return redirect(reverse('events'))  # 削除後にイベント一覧ページにリダイレクト

    return render(request, 'events/delete_event.html', {'event': event})

#イベントの編集
@login_required
def edit_event(request, event_id):
    # 編集対象のイベントを取得
    event = get_object_or_404(Event, id=event_id, team_id=request.user.team)
    
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()  
            return redirect('event_detail', event_id=event.id)  
    else:
        form = EventForm(instance=event)  

    return render(request, 'events/edit_event.html', {'form': form, 'event': event})


# 出欠管理機能
@login_required
def check_attendance(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    attendance, created = Attendance.objects.get_or_create(user_id=request.user, event_id=event)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=attendance)
        if form.is_valid():
            form.save()
            return redirect('event_detail', event_id=event.id)
    else:
        form = AttendanceForm(instance=attendance)

    return render(request, 'events/check_attendance.html', {'event': event, 'form': form})