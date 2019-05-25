from django.core.exceptions import PermissionDenied, FieldDoesNotExist
from .models import VoiceTrack

class UserBalanceTextMixin(object):

	def form_valid(self, form):
		if len(form.cleaned_data['text']) <= self.request.user.balance:
			return super(UserBalanceTextMixin, self).form_valid(form)
		else:
			raise PermissionDenied()