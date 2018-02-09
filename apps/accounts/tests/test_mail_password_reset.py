from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase
from django.urls import reverse


class PasswordResetMailTests(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.response = self.client.post(reverse('accounts:password_reset'), {'email': 'john@doe.com'})
        self.email = mail.outbox[0]

    def test_email_subject(self):
        self.assertEqual('[Django Boards] Please reset your password', self.email.subject)

    def test_email_body(self):
        context = self.response.context
        token = context.get('token')
        uid = context.get('uid')
        password_reset_token_url = reverse('accounts:password_reset_confirm', kwargs={
            'uidb64': uid,
            'token': token
        })
        self.assertIn(password_reset_token_url, self.email.body)
        self.assertIn('john', self.email.body)
        self.assertIn('john@doe.com', self.email.body)

    def test_email_to(self):
        self.assertEqual(['john@doe.com',], self.email.to)
