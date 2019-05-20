import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView

from core.forms import VoiceTrackCreationForm
from core.models import VoiceTrack


# Create your views here.
class CreateMessageView(LoginRequiredMixin, CreateView):

    form_class = VoiceTrackCreationForm
    template_name = 'main.html'

    def get_success_url(self):
        return reverse('core:main')

    def get_initial(self):
        return {
            'owner': self.request.user.id,
        }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tracks = self.request.user.tracks()
        ctx.update({
            'tracks': tracks,
        })
        return ctx

    

    