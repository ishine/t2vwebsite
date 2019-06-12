from unittest.mock import patch

import factory
from django.contrib.auth import get_user_model
from .models import VoiceTrack


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Sequence(lambda n: 'user%d' % n)


class VoiceTrackFactory(factory.DjangoModelFactory):
    text = factory.Sequence(lambda n: 'foo%d' % n)

    pitch = 0
    speed = 1
    language = "EN"
    voice = "AM"

    class Meta:
        model = VoiceTrack
