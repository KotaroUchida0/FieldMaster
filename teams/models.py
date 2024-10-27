from django.db import models

# Create your models here.
from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=100, verbose_name='チーム名')
    joined_datetime = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
    updated_datetime = models.DateTimeField(auto_now=True, verbose_name='更新日時')

    def __str__(self):
        return self.team_name
    
    class Meta:
        db_table = 'teams'

