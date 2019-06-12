import base64
import json
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .factories import VoiceTrackFactory, UserFactory
from .models import VoiceTrack

import core.views as views


class VoiceTrackCreationTestCase(TestCase):

    def test_calling_create_queues_confirmation_email_task(self):

        track = VoiceTrackFactory(text='foo', owner=UserFactory())

        self.assertEqual(VoiceTrack.objects.get(text='foo'), track)


class UserActiveManagerTestCase(TestCase):

    def testConfirmedSubscribersForMailingList(self):

        confirmed_users = [
            UserFactory(is_active=True)
            for n in range(3)]

        unconfirmed_users = [
            UserFactory(is_active=False)
            for n in range(3)]

        confirmed_users_all = get_user_model().objects.all()

        confirmed_users_active = get_user_model().objects.filter(is_active=True)

        confirmed_users_false = get_user_model().objects.filter(is_active=False)

        self.assertEqual(len(confirmed_users_all), 6)

        for user in confirmed_users_active:
            self.assertIn(user, confirmed_users)

        for user in confirmed_users_false:
            self.assertIn(user, unconfirmed_users)


class MainTestCase(TestCase):
    """
    Tests the MainPage view
    """

    REQUEST = RequestFactory().get(path='/')

    def test_GET_on_day_with_no_questions(self):
        response = views.MainPage.as_view()(
            self.REQUEST,
        )
        self.assertEqual(200, response.status_code)
        self.assertEqual(['main.html'],
                         response.template_name)
        self.assertContains(
            response, '< form action="create_voice/" method="post" id="voice_form" >')


class TestAPI(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()
        self.view = views.VoiceTrackList.as_view()
        self.uri = '/api/voice/list/'
        self.user = UserFactory()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_list(self):
        request = self.factory.get(self.uri,
                                   HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_listing_all_my_voice_lists(self):
        voice_lists = [
            VoiceTrackFactory(owner=self.user)
            for i in range(3)
        ]

        request = self.factory.get('/api/voice/list/',
                                   HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        response.render()
        self.assertEqual(200, response.status_code)
        parsed = json.loads(response.content)
        self.assertEqual(3, len(parsed))

        content = str(response.content)

        for ml in voice_lists:
            self.assertIn(str(ml.id), content)
            self.assertIn(ml.text, content)
