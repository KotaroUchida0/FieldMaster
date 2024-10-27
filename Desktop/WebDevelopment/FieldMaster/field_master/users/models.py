from django.db import models
from django.contrib.auth.models import AbstractUser
from teams.models import Team  # チームモデルのインポート
# Create your models here.

class CustomUser(AbstractUser):
    # 不要なフィールドを削除
    first_name = None
    last_name = None
    is_staff = None

    # 必要なフィールドを追加
    POSITION_CHOICES = [
        ('P', 'ピッチャー'),
        ('C', 'キャッチャー'),
        ('IF', '内野手'),
        ('OF', '外野手'),
    ]

    BAT_THROW_CHOICES = [
        ('RR', '右投げ右打ち'),
        ('RL', '右投げ左打ち'),
        ('LR', '左投げ右打ち'),
        ('LL', '左投げ左打ち'),
    ]

    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # 必要なら追加。例: ['username']
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name='所属チーム', related_name='members')
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, verbose_name='ポジション')
    role = models.CharField(max_length=50, blank=True, null=True, verbose_name='役割')
    bat_throw = models.CharField(max_length=2, choices=BAT_THROW_CHOICES,  verbose_name='投打')
    jersey_number = models.IntegerField(blank=True, null=True, verbose_name='背番号')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.username