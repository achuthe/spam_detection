from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Contact

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            phone_number='+123456789',
            email='testuser@example.com',
            password='password123'
        )
        self.client.login(username='testuser', password='password123')

    def test_register_user(self):
        url = reverse('register')
        data = {
            "username": "newuser",
            "phone_number": "+1122334455",
            "email": "newuser@example.com",
            "password": "password123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_contacts(self):
        self.client.force_authenticate(user=self.user)  # Ensure the user is authenticated
        url = reverse('contact-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


