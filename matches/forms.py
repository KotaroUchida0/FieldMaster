from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['score_team', 'score_opponent', 'result', 'description']
        labels = {
            'score_team': '自チームのスコア',
            'score_opponent': '相手チームのスコア',
            'result': '結果',
            'description': '試合内容',
        }