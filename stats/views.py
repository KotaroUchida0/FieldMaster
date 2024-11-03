from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import HitterStatFormSet, PitcherStatFormSet
from .models import HitterStat, PitcherStat
from matches.models import Match

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
