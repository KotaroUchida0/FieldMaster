from django.db import models
from django.conf import settings
from teams.models import Team

# Create your models here.
class Event(models.Model):
    EVENT_TYPES = [
        ('practice', '練習'),
        ('game', '試合'),
    ]
    
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES, verbose_name='イベントタイプ')
    title = models.CharField(max_length=100, verbose_name='タイトル')
    date = models.DateField(verbose_name='日付')
    time = models.TimeField(verbose_name='時間')
    location = models.CharField(max_length=100, verbose_name='場所')
    detail = models.TextField(verbose_name='詳細', blank=True)
    team_id = models.ForeignKey(
        'teams.Team',
        on_delete=models.CASCADE,
        verbose_name='チーム',
        db_column='team_id',
        related_name='events',
        null=True,  # リレーションを定義
    )

    def __str__(self):
        return f"{self.title} - {self.date} {self.time}"

    class Meta:
        db_table = 'events'

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', '出席'),
        ('absent', '欠席'),
        ('undecided', '未定'),
    ]

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='ユーザー',
        db_column='user_id',
        related_name='attendances'  # リレーションを定義
    )
    event_id = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        verbose_name='イベント',
        db_column='event_id',
        related_name='attendances'  # リレーションを定義
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='ステータス')

    def __str__(self):
        return f"{self.user_id.username} - {self.event_id.title} - {self.status}"

    class Meta:
        db_table = 'attendance'
        unique_together = ('user_id', 'event_id')  # ユーザーとイベントの組み合わせが重複しないように設定
