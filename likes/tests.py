# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Like
from highlights.models import Highlight
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LikesTest(APITestCase):
    def setUp(self):
        """
        Set up the tests by creating 2 users and a highlight
        """
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
            title='Test Title 1',
            description='Test Description 1',
            improve='Test Improve',
            category='family-and-friends',
        )
        Highlight.objects.create(
            owner=test_user2,
            title='Test Title 2',
            description='Test Description 2',
            improve='Test Improve',
            category='family-and-friends',
        )

    def test_non_logged_in_user_cannot_like(self):
        """
        Test that a non logged in user cannot like a highlight
        """
        response = self.client.post('/likes/', {
            'highlight_id': 1
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_like_someone_elses_highlight(self):
        """
        Test that a logged in user can like a different users highlight
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/likes/', {
            'highlight': 2
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        like_count = Like.objects.all().count()
        self.assertEqual(like_count, 1)

    def test_user_can_unlike_a_highlight(self):
        """
        Test that a user can unlike a highlight
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/likes/', {
            'highlight': 2
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        like_count = Like.objects.all().count()
        self.assertEqual(like_count, 1)
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        second_like_count = Like.objects.all().count()
        self.assertEqual(second_like_count, 0)

    def test_user_cannot_unlike_another_users_like(self):
        """
        Test that a user cannot unlike another user's like
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/likes/', {
            'highlight': 2
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        like_count = Like.objects.all().count()
        self.assertEqual(like_count, 1)
        self.client.login(username='testuser2', password='testpassword')
        response = self.client.delete('/likes/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        second_like_count = Like.objects.all().count()
        self.assertEqual(second_like_count, 1)
