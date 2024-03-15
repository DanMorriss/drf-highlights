# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Highlight
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class HighlightDetailViewTest(APITestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(
            username='testuser1',
            password='testpassword'
        )
        test_user2 = User.objects.create_user(
            username='testuser2',
            password='testpassword'
        )
        Highlight.objects.create(
            owner=test_user1,
            title='Test Title',
            description='Test Description',
            improve='Test Improve',
            category='family-and-friends',
        )

    def test_can_get_highlight_by_id(self):
        response = self.client.get('/highlights/1/')
        self.assertEqual(response.data['title'], 'Test Title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_get_highlight_with_invalid_id(self):
        response = self.client.get('/highlights/100/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_their_own_post(self):
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.put('/highlights/1/', {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'improve': 'Updated Improve',
            'category': 'pets-and-animals',
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_someone_elses_post(self):
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.put('/highlights/1/', {
            'title': 'Updated Title',
            'description': 'Updated Description',
            'improve': 'Updated Improve',
            'category': 'pets-and-animals',
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
