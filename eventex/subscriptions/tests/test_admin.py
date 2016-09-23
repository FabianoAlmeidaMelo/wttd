from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.admin import (
    admin,
    SubscriptionModelAdmin,
    )
from eventex.subscriptions.models import Subscription

from unittest.mock import Mock

class SubscriptionModelAdminTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Fabiano Almeida',
                                   cpf='12345678901',
                                   email='email@uol.com',
                                   phone='12-982239764')
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """
        Action mark_as_paid shoud be instaled
        """
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """
        It should mark all subscriptions as paid
        """
        self.call_action()
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())

    def test_mesage(self):
        """
        It should message to user.
        """
        mock = self.call_action()
        mock.assert_called_once_with(None, '1 inscrição foi marcada como paga.')

    def call_action(self):
        queryset = Subscription.objects.all()
        mock = Mock()
        old_message_user = SubscriptionModelAdmin.message_user
        SubscriptionModelAdmin.message_user = mock

        self.model_admin.mark_as_paid(None, queryset)
        SubscriptionModelAdmin.message_user = old_message_user

        return mock
