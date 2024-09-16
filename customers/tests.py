from django.test import TestCase
from rest_framework import status
from oauth2_provider.models import Application
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Customer


class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.client_id = 'test-client-id'
        self.client_secret = 'test-client-secret'
        self.application = Application.objects.create(
            name='Test Application',
            client_type='confidential',
            authorization_grant_type='password',
            client_id=self.client_id,
            client_secret=self.client_secret,
            user=self.user
        )

        self.client = APIClient()
        self.oauth2_token = self.get_oauth2_token()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.oauth2_token)
        # self.client.login(username='testuser', password='testpass')

    def get_oauth2_token(self):
        response = self.client.post('/auth/token/', {
            'grant_type': 'password',
            'username': 'testuser',
            'password': 'testpassword',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        })

        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access_token']

    def test_create_customer(self):
        response = self.client.post('/api/customers/', {
            'name': 'John',
            'surname': 'Doe',
            'customer_id': '12345',
            'photo': 'http://example.com/photo.jpg'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)

    def test_list_customers(self):
        Customer.objects.create(name='Jane', surname='Doe',
                                customer_id='67890', created_by=self.user)
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
