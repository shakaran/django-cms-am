from django.test import TestCase

from .models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='testuser',
            email='testuser@example.com'
        )
        self.user.set_password('password123')
        self.user.save()

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertTrue(self.user.check_password('password123'))

    def test_user_str(self):
        self.assertEqual(str(self.user), 'testuser')

    # Django's User model no enforces unique email addresses in User base model.
    # Uncomment the following test if you want to check for unique email addresses.
    """
    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create(
                username='testuser2',
                email='testuser@example.com',
                password='password123'
            )
    """
