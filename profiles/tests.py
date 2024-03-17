# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Profile
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProfileTest(APITestCase):
    def setUp(self):
        """
        Set up the tests by creating 2 users
        """
        User.objects.create_user(
            username='testuser1',
            password='testpassword'
        )
        User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )

    def test_non_logged_in_user_can_view_existing_profile(self):
        """
        Test that a non logged in user can view a profile
        """
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_view_their_profile(self):
        """
        Test that a logged in user can view their profile
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_can_view_other_users_profile(self):
        """
        Test that a logged in user cannot view other users profile
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.get('/profiles/2/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_view_non_existent_profile(self):
        """
        Test that a user cannot view a profile that does not exist
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.get('/profiles/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_username(self):
        """
        Test that a user can update their profiles username
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.put('/profiles/1/', {
            'username': 'new username',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
