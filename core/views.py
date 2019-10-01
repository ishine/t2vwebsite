import logging
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView, TemplateView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from core.forms import VoiceTrackCreationForm
from core.models import VoiceTrack
from core.serializers import VoiceTrackSerializer
from core.mixins import UserBalanceTextMixin
from core.permissions import UserBalanceTextPermission, UserCanUseVoiceTrack


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


class CreateMessageView(LoginRequiredMixin, UserBalanceTextMixin, CreateView):

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


'''
____________________________

REST API VIEWS
____________________________

'''


class VoiceTrackCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, UserBalanceTextPermission)
    serializer_class = VoiceTrackSerializer

    def get_serializer(self, *args, **kwargs):
        data = kwargs.get('data', None)
        if data:
            new_data = dict(data)
            new_data['owner'] = self.request.user.id
            kwargs['data'] = new_data
        return super().get_serializer(*args, **kwargs)


class VoiceTrackDetail(APIView):
    permission_classes = (IsAuthenticated, UserCanUseVoiceTrack)

    def get_object(self, pk):
        try:
            return VoiceTrack.objects.get(pk=pk)
        except VoiceTrack.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):

        snippet = self.get_object(pk)
        self.check_object_permissions(self.request, snippet)
        serializer = VoiceTrackSerializer(snippet)
        return Response(serializer.data)


class VoiceTrackList(generics.ListCreateAPIView):

    serializer_class = VoiceTrackSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        return VoiceTrack.objects.all().filter(owner=self.request.user)

    def list(self, request):

        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = VoiceTrackSerializer(queryset, many=True)
        return Response(serializer.data)
