from django import forms
from .models import HitterStat, PitcherStat
from users.models import CustomUser
from django.forms import modelformset_factory

class HitterStatForm(forms.ModelForm):
    class Meta:
        model = HitterStat
        fields = [
            'player', 'position', 'order', 'plate_appearances', 
            'at_bats', 'hits', 'doubles', 'triples', 'home_runs', 'rbi', 
            'runs', 'strikeouts', 'walks', 'hbp', 'sac_bunt', 'sac_fly', 
            'steals', 'caught_stealing', 'gdp', 'errors'
        ]
        widgets = {
            'player': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'plate_appearances': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'at_bats': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'hits': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'doubles': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'triples': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'home_runs': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'rbi': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'runs': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'strikeouts': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'walks': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'hbp': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'sac_bunt': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'sac_fly': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'steals': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'caught_stealing': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'gdp': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'errors': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),}

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)  
        super().__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = CustomUser.objects.filter(team=team)

    def clean(self):
        cleaned_data = super().clean()
        default_zero_fields = [
            'plate_appearances', 'at_bats', 'hits', 'doubles', 'triples', 'home_runs', 'rbi', 
            'runs', 'strikeouts','walks', 'hbp', 'sac_bunt', 'sac_fly', 'steals', 'caught_stealing', 'gdp', 'errors'
        ]
        for field in default_zero_fields:
            if not cleaned_data.get(field):  
                cleaned_data[field] = 0
        return cleaned_data

HitterStatFormSet = modelformset_factory(
    HitterStat,
    form=HitterStatForm,
    extra=1
)

class PitcherStatForm(forms.ModelForm):
    class Meta:
        model = PitcherStat
        fields = [
            'player', 'innings_pitched', 'plate_appearances', 
            'at_bats', 'hits_allowed', 'doubles_allowed', 'triples_allowed', 'home_runs_allowed', 'strikeouts', 
            'walks', 'hbp', 'runs_allowed', 'earned_runs', 'wild_pitches', 'starter', 
            'complete_game', 'shutout', 'wins', 'losses', 'saves', 'balks'
        ]
        widgets = {
            'player': forms.Select(attrs={'class': 'form-control'}),
            'innings_pitched': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1'}),
            'plate_appearances': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'at_bats': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'hits_allowed': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'doubles_allowed': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'triples_allowed': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'home_runs_allowed': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'strikeouts': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'walks': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'hbp': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'runs_allowed': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'earned_runs': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'wild_pitches': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'starter': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'complete_game': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'shutout': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'wins': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'losses': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'saves': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'balks': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
        }

    def __init__(self, *args, **kwargs):
        team = kwargs.pop('team', None)  
        super().__init__(*args, **kwargs)
        if team:
            self.fields['player'].queryset = CustomUser.objects.filter(team=team)

    def clean(self):
        cleaned_data = super().clean()
        default_zero_fields = [
            'plate_appearances', 'at_bats', 'hits_allowed', 'doubles_allowed', 'triples_allowed', 'home_runs_allowed', 
            'strikeouts','walks', 'hbp', 'runs_allowed', 'earned_runs', 'wild_pitches', 'starter', 'complete_game', 'shutout',
            'wins', 'losses', 'saves', 'balks'
            ]
        for field in default_zero_fields:
            if not cleaned_data.get(field):  
                cleaned_data[field] = 0
        return cleaned_data

PitcherStatFormSet = modelformset_factory(
    PitcherStat,
    form=PitcherStatForm,
    extra=1
)