from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Customer

class CustomerAPITestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_create_customer(self):
        response = self.client.post('/api/customers/', {
            'name': 'John',
            'surname': 'Doe',
            'customer_id': '12345'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Customer.objects.count(), 1)

    def test_list_customers(self):
        Customer.objects.create(name='Jane', surname='Doe', customer_id='67890', created_by=self.user)
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)