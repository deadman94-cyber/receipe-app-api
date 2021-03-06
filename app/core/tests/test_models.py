from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_email_success(self):

        email = 'test@lodondappdev.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_noramilze(self):

        email = "test@LONDON.COM"
        user = get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())    


    def test_new_user_invalid_email(self):

        with self.assertRaises(ValueError):

            get_user_model().objects.create_user(None,'test@123')
    
    def test_create_superuser(self):

        user=get_user_model().objects.create_superuser(
            'admin@a.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)