import uuid
import logging
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models import F
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

# Create your models here.
# Language choices
ENGLISH = 'EN'
LANGUAGES = (
	(ENGLISH, 'English'),
)
# Voice choices
AMANDA = 'AM'
VOICES = (
	(AMANDA, 'Amanda'),
)


class VoiceTrack(models.Model):

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

	created = models.DateTimeField(auto_now_add=True)
 
	text = models.CharField(max_length=999999)

	owner = models.ForeignKey(to=settings.AUTH_USER_MODEL,
							  on_delete=models.CASCADE,
							  related_name='tracks')

	audio = models.FileField(upload_to='audio/', blank=True)

	duration =  models.IntegerField(default=0)

	pitch = models.SmallIntegerField(default=0)

	speed = models.FloatField(default=1)

	language = models.CharField(max_length=2,
								choices=LANGUAGES,
								default=ENGLISH,)

	voice = models.CharField(max_length=2,
							 choices=VOICES,
							 default=AMANDA,)

	def __str__(self):
		
		return self.text[:15]

	def user_have_enough_balance(self, user):
		return len(self.text) <= user.balance		

	def user_have_permis(self, user):
		return user == self.owner

	class Meta:
		ordering = ['-created']

	def save(self, force_insert=False, force_update=False, using=None,
			 update_fields=None):
		is_new = self._state.adding or force_insert
		
		# Desrising balance of user
		number_of_symbols = len(self.text)
		own = get_user_model().objects.get(id = self.owner.id)
		own.balance = F("balance") - number_of_symbols
		own.save()

		super().save(force_insert=force_insert, force_update=force_update,
					 using=using, update_fields=update_fields)
		logger.info("in save, this should be true. is_new:%s" % (is_new))
		