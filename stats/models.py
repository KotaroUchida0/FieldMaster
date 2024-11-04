from django.db import models
from teams.models import Team
from matches.models import Match
from users.models import CustomUser

class HitterStat(models.Model):
    POSITION_CHOICES = [
        ('P', 'ピッチャー'),
        ('C', 'キャッチャー'),
        ('1B', 'ファースト'),
        ('2B', 'セカンド'),
        ('3B', 'サード'),
        ('SS', 'ショート'),
        ('LF', 'レフト'),
        ('CF', 'センター'),
        ('RF', 'ライト'),
        ('DH', 'DH'),
    ]
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="選手")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name="試合")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="チーム")
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name="ポジション")
    order = models.IntegerField(verbose_name="打順")
    plate_appearances = models.IntegerField(verbose_name="打席数", default=0)
    at_bats = models.IntegerField(verbose_name="打数", default=0)
    hits = models.IntegerField(verbose_name="ヒット", default=0)
    doubles = models.IntegerField(verbose_name="二塁打", default=0)
    triples = models.IntegerField(verbose_name="三塁打", default=0)
    home_runs = models.IntegerField(verbose_name="本塁打", default=0)
    rbi = models.IntegerField(verbose_name="打点", default=0)
    runs = models.IntegerField(verbose_name="得点", default=0)
    strikeouts = models.IntegerField(verbose_name="三振", default=0)
    walks = models.IntegerField(verbose_name="四球", default=0)
    hbp = models.IntegerField(verbose_name="死球", default=0)
    sac_bunt = models.IntegerField(verbose_name="犠打", default=0)
    sac_fly = models.IntegerField(verbose_name="犠飛", default=0)
    steals = models.IntegerField(verbose_name="盗塁", default=0)
    caught_stealing = models.IntegerField(verbose_name="盗塁死", default=0)
    gdp = models.IntegerField(verbose_name="併殺打", default=0)
    errors = models.IntegerField(verbose_name="失策", default=0)

    def __str__(self):
        return f"{self.player.name} - {self.match.date}"

    class Meta:
        db_table = 'hitter_stats'


class PitcherStat(models.Model):
    player = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="選手")
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name="試合")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="チーム")
    innings_pitched = models.FloatField(verbose_name="投球回")
    plate_appearances = models.IntegerField(verbose_name="打席数", default=0)
    at_bats = models.IntegerField(verbose_name="打数", default=0)
    hits_allowed = models.IntegerField(verbose_name="被安打", default=0)
    doubles_allowed = models.IntegerField(verbose_name="被二塁打", default=0)
    triples_allowed = models.IntegerField(verbose_name="被三塁打", default=0)
    home_runs_allowed = models.IntegerField(verbose_name="被本塁打", default=0)
    strikeouts = models.IntegerField(verbose_name="三振", default=0)
    walks = models.IntegerField(verbose_name="四球", default=0)
    hbp = models.IntegerField(verbose_name="死球", default=0)
    runs_allowed = models.IntegerField(verbose_name="失点", default=0)
    earned_runs = models.IntegerField(verbose_name="自責点", default=0)
    wild_pitches = models.IntegerField(verbose_name="暴投", default=0)
    starter = models.BooleanField(default=False, verbose_name="先発")
    complete_game = models.BooleanField(default=False, verbose_name="完投")
    shutout = models.BooleanField(default=False, verbose_name="完封")
    wins = models.IntegerField(verbose_name="勝利", default=0)
    losses = models.IntegerField(verbose_name="敗戦", default=0)
    saves = models.IntegerField(verbose_name="セーブ", default=0)
    balks = models.IntegerField(verbose_name="ボーク", default=0)

    def __str__(self):
        return f"{self.player.name} - {self.match.date}"

    class Meta:
        db_table = 'pitcher_stats'