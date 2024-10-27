from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), 
        label="日付"
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}), 
        label="時間"
    )

    class Meta:
        model = Event
        fields = ['event_type', 'title', 'date', 'time', 'location', 'detail']
