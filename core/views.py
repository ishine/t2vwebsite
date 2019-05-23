import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView, TemplateView

from core.forms import VoiceTrackCreationForm
from core.models import VoiceTrack


# Create your views here.
class MainPage(TemplateView):

    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        form_class = VoiceTrackCreationForm
        ctx.update({
            'form': form_class,
        })

        if self.request.user.is_authenticated:
            tracks = self.request.user.tracks.all()
            balance = self.request.user.balance
            ctx.update({
                'tracks': tracks,
                'balance': balance,
            })

        
        return ctx


class CreateMessageView(LoginRequiredMixin, CreateView):

    form_class = VoiceTrackCreationForm

    def get_success_url(self):
        return reverse('core:MainPage')

    def get_initial(self):
        return {
            'owner': self.request.user.id,
        }

class DeleteMassageView(LoginRequiredMixin, DeleteView):
    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)
    model = VoiceTrack

    def get_success_url(self):
        return reverse('core:MainPage')

    