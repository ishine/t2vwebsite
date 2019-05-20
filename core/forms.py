from django import forms
from django.contrib.auth import get_user_model

from core.models import VoiceTrack

class VoiceTrackCreationForm(forms.ModelForm):
	owner = forms.ModelChoiceField(
        widget=forms.HiddenInput,
        queryset=get_user_model().objects.all(),
        disabled=True,
    )

    class Meta:
        model = VoiceTrack
        fields = ['text', 'owner', 'pitch', 'speed', 'language', 'voice',]