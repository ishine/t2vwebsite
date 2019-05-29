from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import VoiceTrack


class VoiceTrackSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(
		queryset=get_user_model().objects.all())

	class Meta:
		model = VoiceTrack
		fields = ('id',
			'text', 
			'audio', 
			'duration', 
			'created', 
			'owner', 
			'pitch', 
			'speed', 
			'language', 
			'voice',)
		read_only_fields = ('id', 'duration', 'created', )
		
		extra_kwargs = {
            'audio': {'allow_null': True, 'required': False},
            'duration': {'allow_null': True, 'required': False},
        }