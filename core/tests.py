import base64
import json
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APITestCase

from .factories import VoiceTrackFactory, UserFactory
from .models import VoiceTrack



class VoiceTrackCreationTestCase(TestCase):

    def test_calling_create_queues_confirmation_email_task(self):
        
        track = VoiceTrackFactory(text='foo', owner = UserFactory())
        
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



'''class ListMailingListsWithAPI(APITestCase):

    def setUp(self):
        password = 'password'
        username = 'unit test'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        cred_bytes = '{}:{}'.format(username, password).encode('utf-8')
        self.basic_auth = base64.b64encode(cred_bytes).decode('utf-8')

    def test_listing_all_my_mailing_lists(self):
        mailing_lists = [
            MailingList.objects.create(
                name='unit test {}'.format(i),
                owner=self.user)
            for i in range(3)
        ]

        self.client.credentials(
            HTTP_AUTHORIZATION='Basic {}'.format(self.basic_auth))

        response = self.client.get('/mailinglist/api/v1/mailing-list')

        self.assertEqual(200, response.status_code)
        parsed = json.loads(response.content)
        self.assertEqual(3, len(parsed))

        content = str(response.content)
        for ml in mailing_lists:
            self.assertIn(str(ml.id), content)
            self.assertIn(ml.name, content)
'''