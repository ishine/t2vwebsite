from django import forms
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator
from core.models import VoiceTrack, LANGUAGES, VOICES


class VoiceTrackCreationForm(forms.ModelForm):
	owner = forms.ModelChoiceField(
		widget=forms.HiddenInput,
		queryset=get_user_model().objects.all(),
		disabled=True,
	)

	text = forms.CharField(
			widget=forms.Textarea(attrs={'class': 'text-input-place',
										 'placeholder': 'Text',
										 'cols': '30',
										 'rows': '5',
										 }),
			validators=[MinLengthValidator(0), MaxLengthValidator(999999)],
			required=True,
		)

	pitch = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 
														'name' : 'rangeInput',
														'onchange' : 'updateTextInput(this.value);',
														'value' : '0',
														'min' : '-20',
														'max' : '20',
														}),
								validators=[MinValueValidator(-20), MaxValueValidator(20)],
								required=True,)

	speed = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 
														'name' : 'rangeInput2',
														'onchange' : 'updateTextInput2(this.value);',
														'value' : '1',
														'step' : '0.05',
														'min' : '0.25',
														'max' : '2',
														}),
								validators=[MinValueValidator(0.25), MaxValueValidator(2)],
								required=True,)

	language = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select-css',}),
			choices = LANGUAGES,
			required=True,
		)

	voice = forms.ChoiceField(widget=forms.Select(attrs={'class': 'select-css',}),
			choices = VOICES,
			required=True,
		)


	class Meta:
		model = VoiceTrack
		fields = ['text', 'owner', 'pitch', 'speed', 'language', 'voice',]
