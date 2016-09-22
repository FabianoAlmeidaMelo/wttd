from django.core import mail
from django.shortcuts import resolve_url
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Fabiano Almeida", cpf='12345678901',
                    email='falmeidamelo@uol.com.br', phone='12-98223-9764')
        self.client.post(resolve_url('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        """3: verifica subject do email"""
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        """4: verifica o sender email"""
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        """5: verifica destinatario do email"""
        expect = ['contato@eventex.com.br', 'falmeidamelo@uol.com.br']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        """6: verifica corpo do email"""
        contents = [
                    'Fabiano Almeida',
                    '12345678901',
                    'falmeidamelo@uol.com.br',
                    '12-98223-9764'
                ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
        # self.assertIn('Fabiano Almeida', self.email.body)
        # self.assertIn('12345678901', self.email.body)
        # self.assertIn('falmeidamelo@uol.com.br', self.email.body)
        # self.assertIn('12-98223-9764', self.email.body)
