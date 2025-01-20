from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import HitterStatFormSet, PitcherStatFormSet
from .models import HitterStat, PitcherStat
from matches.models import Match
from django.db.models import Sum, F, FloatField
from django.db.models.functions import Coalesce
from django.db.models.functions import ExtractYear

@login_required
def create_hitter_stats(request, match_id):
    user_team = request.user.team  

    if request.method == 'POST':
        formset = HitterStatFormSet(request.POST, form_kwargs={'team': user_team})
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.team = user_team
                instance.match_id = match_id  
                instance.save()
            return redirect(reverse('match_detail', args=[match_id]))
        else:
            print(formset.errors)
    else:
        formset = HitterStatFormSet(queryset=HitterStat.objects.none(), form_kwargs={'team': user_team})

    return render(request, 'stats/hitter_stats_form.html', {'formset': formset})

@login_required
def create_pitcher_stats(request, match_id):
    user_team = request.user.team  

    if request.method == 'POST':
        formset = PitcherStatFormSet(request.POST, form_kwargs={'team': user_team})
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.team = user_team
                instance.match_id = match_id  
                instance.save()
            return redirect(reverse('match_detail', args=[match_id]))
        else:
            print(formset.errors)
    else:
        formset = PitcherStatFormSet(queryset=PitcherStat.objects.none(), form_kwargs={'team': user_team})

    return render(request, 'stats/pitcher_stats_form.html', {'formset': formset})

@login_required
def total_stats(request):
    user_team = request.user.team

    # 通算成績
    hitter_totals = HitterStat.objects.filter(team=user_team).values('player__username').annotate(
        plate_appearances=Sum('plate_appearances'),
        at_bats=Sum('at_bats'),
        hits=Sum('hits'),
        doubles=Sum('doubles'),
        triples=Sum('triples'),
        home_runs=Sum('home_runs'),
        rbi=Sum('rbi'),
        runs=Sum('runs'),
        strikeouts=Sum('strikeouts'),
        walks=Sum('walks'),
        hbp=Sum('hbp'),
        sac_bunt=Sum('sac_bunt'),
        sac_fly=Sum('sac_fly'),
        steals=Sum('steals'),
        caught_stealing=Sum('caught_stealing'),
        gdp=Sum('gdp'),
        errors=Sum('errors')
    )

    pitcher_totals = PitcherStat.objects.filter(team=user_team).values('player__username').annotate(
        innings_pitched=Sum('innings_pitched'),
        plate_appearances=Sum('plate_appearances'),
        at_bats=Sum('at_bats'),
        hits_allowed=Sum('hits_allowed'),
        doubles_allowed=Sum('doubles_allowed'),
        triples_allowed=Sum('triples_allowed'),
        home_runs_allowed=Sum('home_runs_allowed'),
        strikeouts=Sum('strikeouts'),
        walks=Sum('walks'),
        hbp=Sum('hbp'),
        runs_allowed=Sum('runs_allowed'),
        earned_runs=Sum('earned_runs'),
        wild_pitches=Sum('wild_pitches'),
        wins=Sum('wins'),
        losses=Sum('losses'),
        saves=Sum('saves'),
        balks=Sum('balks')
    )

    # 年度別成績
    hitter_yearly_stats = HitterStat.objects.filter(team=user_team).annotate(
        year=ExtractYear('match__event__date')
    ).values('year', 'player__username').annotate(
        plate_appearances=Sum('plate_appearances'),
        at_bats=Sum('at_bats'),
        hits=Sum('hits'),
        doubles=Sum('doubles'),
        triples=Sum('triples'),
        home_runs=Sum('home_runs'),
        rbi=Sum('rbi'),
        runs=Sum('runs'),
        strikeouts=Sum('strikeouts'),
        walks=Sum('walks'),
        hbp=Sum('hbp'),
        sac_bunt=Sum('sac_bunt'),
        sac_fly=Sum('sac_fly'),
        steals=Sum('steals'),
        caught_stealing=Sum('caught_stealing'),
        gdp=Sum('gdp'),
        errors=Sum('errors')
    ).order_by('year', 'player__username')

    pitcher_yearly_stats = PitcherStat.objects.filter(team=user_team).annotate(
        year=ExtractYear('match__event__date')
    ).values('year', 'player__username').annotate(
        innings_pitched=Sum('innings_pitched'),
        plate_appearances=Sum('plate_appearances'),
        at_bats=Sum('at_bats'),
        hits_allowed=Sum('hits_allowed'),
        doubles_allowed=Sum('doubles_allowed'),
        triples_allowed=Sum('triples_allowed'),
        home_runs_allowed=Sum('home_runs_allowed'),
        strikeouts=Sum('strikeouts'),
        walks=Sum('walks'),
        hbp=Sum('hbp'),
        runs_allowed=Sum('runs_allowed'),
        earned_runs=Sum('earned_runs'),
        wild_pitches=Sum('wild_pitches'),
        wins=Sum('wins'),
        losses=Sum('losses'),
        saves=Sum('saves'),
        balks=Sum('balks')
    ).order_by('year', 'player__username')

    context = {
        'hitter_totals': hitter_totals,
        'pitcher_totals': pitcher_totals,
        'hitter_yearly_stats': hitter_yearly_stats,
        'pitcher_yearly_stats': pitcher_yearly_stats
    }
    return render(request, 'stats/total_stats.html', context)


@login_required
def title_page(request):
    user_team = request.user.team  
    # 打率上位3選手
    hitter_avg = HitterStat.objects.filter(player__team=user_team).values('player__username').annotate(
        avg=Coalesce(F('hits') / F('at_bats'), 0, output_field=FloatField())
    ).order_by('-avg')[:3]

    # 本塁打数上位3選手
    homerun_leaders = HitterStat.objects.filter(player__team=user_team).values('player__username').annotate(
        total_home_runs=Sum('home_runs')
    ).order_by('-total_home_runs')[:3]

    # 投手の勝利数上位3選手
    win_leaders = PitcherStat.objects.filter(player__team=user_team).values('player__username').annotate(
        total_wins=Sum('wins')
    ).order_by('-total_wins')[:3]

    # 投手の奪三振数上位3選手
    strikeout_leaders = PitcherStat.objects.filter(player__team=user_team).values('player__username').annotate(
        total_strikeouts=Sum('strikeouts')
    ).order_by('-total_strikeouts')[:3]

    context = {
        'hitter_avg': hitter_avg,
        'homerun_leaders': homerun_leaders,
        'win_leaders': win_leaders,
        'strikeout_leaders': strikeout_leaders
    }
    return render(request, 'stats/title_page.html', context)