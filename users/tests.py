from django.test import TestCase

from .models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com',
            password='password123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(
                username='testuser2',
                email='testuser@example.com',
                password='password123'
            )
