from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscritionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(name='Fabiano Almeida',
                                          email='fabiano@email.com',
                                          phone='12-982239764',
                                          cpf='12345678901')
        self.response = self.client.get('/inscricao/{}/'.format(self.obj.pk))


    def test_get(self):
        """1: GET /detail/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """2: Must use subscription/suscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = ('Fabiano Almeida',
                    'fabiano@email.com',
                    '12-982239764',
                    '12345678901')
        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)

class SubscritionDetailNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get('/inscricao/0/')
        self.assertEqual(404, response.status_code)
