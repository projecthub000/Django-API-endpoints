# profiles/tests.py

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class ProfileAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_profile(self):
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'bio': 'Lorem ipsum dolor sit amet.',
            'profile_picture': None  # Set the profile picture if needed
        }

        response = self.client.post('/api/profile/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'John Doe')
        self.assertEqual(response.data['email'], 'john.doe@example.com')

    def test_update_profile(self):
        data = {
            'bio': 'Updated bio.',
        }

        response = self.client.patch('/api/profile/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['bio'], 'Updated bio.')

    def test_invalid_profile_data(self):
        data = {
            'name': '',  # Invalid, name field is required
            'email': 'invalid_email',  # Invalid, email format is incorrect
        }

        response = self.client.post('/api/profile/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('email', response.data)

    def test_unauthenticated_user(self):
        self.client.logout()
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'bio': 'Lorem ipsum dolor sit amet.',
            'profile_picture': None
        }

        response = self.client.post('/api/profile/', data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

