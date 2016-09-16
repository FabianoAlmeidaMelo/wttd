from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        """
        python manage.py test subscriptions/tests/test_models_subscription.py
        """
        self.obj = Subscription(name='Fabiano Almeida',
                                cpf='12345678901',
                                email='email@uol.com',
                                phone='12-982239764')
        self.obj.save()

    def test_create(self):
        """
        TESTE 01: subscriptions/tests/test_models_subscription.py
        """
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """
        TESTE 02: subscriptions/tests/test_models_subscription.py
        Subscription must have an auto creted _at attr
        """
        self.assertIsInstance(self.obj.created_at, datetime)

