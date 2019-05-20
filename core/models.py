import uuid

from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class VoiceTrack(models.Model):
	# Language choices
	ENGLISH = 'EN'
	LANGUAGES = [
		(ENGLISH, 'English'),
	]

	# Voice choices
	AMANDA = 'AM'
	VOICES = [
		(AMANDA, 'Amanda'),
	]

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	created = models.DateTimeField(auto_now_add=True)

	text = models.CharField(max_length=999999)
	owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
							  on_delete=models.CASCADE,
							  related_name='tracks')
	audio = models.FileField(upload_to='audio/')

	pitch = models.SmallIntegerField(default = 0)
	speed = models.SmallIntegerField(default = 1)

	language = models.CharField(max_length=2,
		choices=LANGUAGES,
		default=ENGLISH,)

	voice = models.CharField(max_length=2,
		choices=VOICES,
		default=AMANDA,)

	def __str__(self):
		return self.text[:15]

	def user_have_permis(self, user):
		return user == self.owner
