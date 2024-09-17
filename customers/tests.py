from django.test import TestCase
from rest_framework import status
from oauth2_provider.models import AccessToken, Application
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Customer

from oauthlib.common import generate_token
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from PIL import Image
import random


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
        # print(f"Client ID: {self.application.client_id}")
        # print(f"Client Secret: {self.application.client_secret}")

        tok = generate_token()
        access_token = AccessToken.objects.create(
            user=self.user,
            application=self.application,
            expires=timezone.now() + relativedelta(hours=1),
            token=tok
        )
        return access_token.token

        """ @todo
        response = self.client.post('/auth/token/', {
            'grant_type': 'password',
            'username': 'testuser',
            'password': 'testpassword',
            'client_id': self.application.client_id,
            'client_secret': self.application.client_secret,
        })

        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.data['access_token']
        """

    def create_fake_image(self):
        photo_file = SimpleUploadedFile(
            name='fake_photo.jpg',
            content=b'',
            content_type='image/jpeg'
        )

        image = Image.new('RGB', (100, 100))
        pixels = image.load()
        for i in range(image.width):
            for j in range(image.height):
                pixels[i, j] = (random.randint(0, 255),
                                random.randint(0, 255),
                                random.randint(0, 255))

        image_byte_stream = io.BytesIO()
        image.save(image_byte_stream, format='JPEG')
        image_byte_stream.seek(0)

        photo_file = SimpleUploadedFile(
            name='fake_photo.jpg',
            content=image_byte_stream.read(),
            content_type='image/jpeg'
        )

        return photo_file

    def test_create_customer(self):
        response = self.client.post('/api/customers/', {
            'name': 'John',
            'surname': 'Doe',
            'customer_id': '12345',
            'photo': self.create_fake_image()
        }, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)

        data = response.json()
        self.assertEqual(data['name'], 'John')
        self.assertEqual(data['surname'], 'Doe')
        self.assertEqual(data['customer_id'], '12345')
        self.assertIsNotNone(data['photo'])
        self.assertEqual(data['created_by'], 1)
        self.assertIsNone(data['modified_by'])
        self.assertIsNotNone(data['created_at'])
        self.assertIsNotNone(data['updated_at'])

    def test_list_customers(self):
        Customer.objects.create(name='Jane', surname='Doe',
                                customer_id='67890', created_by=self.user)
        response = self.client.get('/api/customers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_customer(self):
        customer = Customer.objects.create(
            name='John',
            surname='Doe',
            customer_id='12345',
            created_by=self.user
        )

        response = self.client.get(f'/api/customers/{customer.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['name'], 'John')
        self.assertEqual(data['surname'], 'Doe')
        self.assertEqual(data['customer_id'], '12345')
        self.assertEqual(data['created_by'], customer.id)
        self.assertIsNone(data['modified_by'])
        self.assertIsNotNone(data['created_at'])
        self.assertIsNotNone(data['updated_at'])

    def test_update_customer(self):
        customer = Customer.objects.create(
            name='John',
            surname='Doe',
            customer_id='12345',
            created_by=self.user
        )
        response = self.client.put(f'/api/customers/{customer.id}/', {
            'name': 'Jane',
            'surname': 'Smith',
            'customer_id': '54321',
            'photo': self.create_fake_image()
        }, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['name'], 'Jane')
        self.assertEqual(data['surname'], 'Smith')
        self.assertEqual(data['customer_id'], '54321')
        self.assertIsNotNone(data['photo'])
        self.assertEqual(data['created_by'], customer.id)
        self.assertEqual(data['modified_by'], customer.id)
        self.assertIsNotNone(data['created_at'])
        self.assertIsNotNone(data['updated_at'])

    def test_delete_customer(self):
        customer = Customer.objects.create(
            name='John',
            surname='Doe',
            customer_id='12345',
            created_by=self.user
        )
        response = self.client.delete(f'/api/customers/{customer.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Customer.objects.count(), 0)
