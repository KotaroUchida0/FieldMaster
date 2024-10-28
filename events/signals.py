from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Event
from matches.models import Match  

@receiver(post_save, sender=Event)
def create_match_for_game_event(sender, instance, created, **kwargs):
    if created and instance.event_type == 'game':
        Match.objects.create(event=instance, team=instance.team_id)
