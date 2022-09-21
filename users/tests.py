
from rest_framework.test import APITestCase

from users.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user(username='fortune', email='a@a.com', password='abcd1234')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'a@a.com')
        self.assertFalse(user.is_staff)

    def test_creates_super_user(self):
        user = User.objects.create_superuser(username='fortune', email='a@a.com', password='abcd1234')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'a@a.com')
        self.assertTrue(user.is_staff)

    def test_raises_error_when_no_username_is_suplied(self):

        self.assertRaises(ValueError, User.objects.create_user,
                          username="", email='a@a.com', password='abcd1234')

    def test_raises_error_when_no_email_is_suplied(self):

        self.assertRaises(ValueError, User.objects.create_user,
                          username="Fortune", email='', password='abcd1234')

    def test_raises_error_when_no_username_is_suplied_message(self):

        with self.assertRaisesMessage(ValueError, "The given username must be set"):
            User.objects.create_user(
                username="", email='a@a.com', password='abcd1234')

    def test_raises_error_when_no_email_is_suplied_message(self):

        with self.assertRaisesMessage(ValueError, "The given email must be set"):
            User.objects.create_user(
                username="Fortune", email='', password='abcd1234')

    def test_raises_error_when_is_staff_is_false(self):

        self.assertRaises(ValueError, User.objects.create_superuser,
                          username="", email='a@a.com', password='abcd1234', is_staff=False)

    def test_raises_error_when_is_superuser_is_false(self):

        self.assertRaises(ValueError, User.objects.create_superuser,
                          username="", email='a@a.com', password='abcd1234', is_superuser=False)
