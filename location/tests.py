# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Location
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class LocationTest(APITestCase):
    def setUp(self):
        """
        Set up the tests by creating 2 users
        """
        User.objects.create_user(
            username='testuser1',
            password='testpassword'
        )

    def test_user_can_add_a_location(self):
        """
        Test that a user can add a location
        """
        self.client.login(username='testuser1', password='testpassword')
        response = self.client.post('/locations/', {
            'latitude': 1.1,
            'longitude': -1.1,
            'name': 'location 1'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        location_count = Location.objects.all().count()
        self.assertEqual(location_count, 1)

    def test_user_can_delete_location(self):
        """
        Test that a user can delete a location
        """
        self.client.login(username='testuser1', password='testpassword')
        self.client.post('/locations/', {
            'latitude': 1.1,
            'longitude': -1.1,
            'name': 'location 1'
        })
        response = self.client.delete('/locations/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        location_count = Location.objects.all().count()
        self.assertEqual(location_count, 0)

    def test_user_can_rename_location(self):
        """
        Test that a user can rename a location
        """
        self.client.login(username='testuser1', password='testpassword')
        self.client.post('/locations/', {
            'latitude': 1.1,
            'longitude': -1.1,
            'name': 'location 1'
        })
        response = self.client.put('/locations/1/', {
            'latitude': 1.1,
            'longitude': -1.1,
            'name': 'edited location'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        location_count = Location.objects.all().count()
        self.assertEqual(location_count, 1)
