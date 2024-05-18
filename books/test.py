from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TokenGenerationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_token_generation(self):

        self.assertFalse(Token.objects.filter(user=self.user).exists())

        token, created = Token.objects.get_or_create(user=self.user)

        self.assertTrue(created)

        self.assertTrue(Token.objects.filter(user=self.user).exists())

        self.assertEqual(token.user, self.user)

    def test_token_retrieval(self):

        token, created = Token.objects.get_or_create(user=self.user)

        retrieved_token = Token.objects.get(user=self.user)

        self.assertEqual(retrieved_token, token)
