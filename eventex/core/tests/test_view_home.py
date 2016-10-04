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

    def test_speakers(self):
        """Must show keynote speakers"""
        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.response, expected)

    def test_speackers_link(self):
        """Must show keynote speakers  link"""
        expected = 'href="{}#speakers"'.format(resolve_url('home'))
        self.assertContains(self.response, expected)
