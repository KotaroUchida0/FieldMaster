from django.db import models
from events.models import Event
from teams.models import Team

class Match(models.Model):
    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        verbose_name='イベント',
        related_name='match',
        db_column='event_id'
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        null=True,
        verbose_name='チーム',
        related_name='matches',
        db_column='team_id'
    )
    score_team = models.IntegerField(null=True, blank=True, verbose_name='自チームのスコア')
    score_opponent = models.IntegerField(null=True, blank=True, verbose_name='相手チームのスコア')
    result = models.CharField(
        max_length=20,
        choices=[('win', '勝ち'), ('lose', '負け'), ('draw', '引き分け')],
        verbose_name='試合結果'
    )
    description = models.TextField(null=True, blank=True, verbose_name='内容')

    def __str__(self):
        return f"{self.event.title} vs 自チーム on {self.event.date}"

    class Meta:
        db_table = 'matches'
        ordering = ['-event__date'] 