from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Match, Event
from .forms import MatchForm
# Create your views here.

@login_required
def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'matches/match_detail.html', {'match': match})

@login_required
def update_match(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect(reverse('match_list'))
    else:
        form = MatchForm(instance=match)
    return render(request, 'matches/update_match.html', {'form': form, 'match': match})

@login_required
def match_list(request):
    user_team_id = request.user.team_id
    matches = Match.objects.filter(team_id=user_team_id)
    return render(request, 'matches/match_list.html', {'matches': matches})
