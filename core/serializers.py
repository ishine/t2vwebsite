from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import VoiceTrack


class VoiceTrackSerializer(serializers.HyperlinkedModelSerializer):
	owner = serializers.PrimaryKeyRelatedField(
		queryset=get_user_model().objects.all())

	class Meta:
		model = VoiceTrack
		fields = ('text', 
			'audio', 
			'duration', 
			'created', 
			'owner', 
			'pitch', 
			'speed', 
			'language', 
			'voice',)
		read_only_fields = ('duration', 'created', )
		extra_kwargs = {
			'url': {'view_name': 'mailinglist:api-mailing-list-detail'},
			'subscriber_set': {'view_name': 'mailinglist:api-subscriber-detail'},
		}