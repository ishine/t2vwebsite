from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from .models import VoiceTrack


class UserBalanceTextPermission(BasePermission):

	message = 'User does not have enough blance.'

	def has_permission(self, request, view):
		return len(request.data['text']) <= request.user.balance
	

class UserCanUseVoiceTrack(BasePermission):

	message = 'User cant get this track.'

	def has_object_permission(self, request, view, obj):

		user = request.user
		if type(obj) is VoiceTrack:
			return obj.user_have_permis(user)
		return False