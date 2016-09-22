from django.test import TestCase
from django.shortcuts import resolve_url

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('home'))

    def test_get(self):
        """GET / mest return status code 200"""
        # response = self.client.get('/')
        return self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must use index.html"""
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        expected = 'href="{}"'.format(resolve_url('subscriptions:new'))
        self.assertContains(self.response, expected)
