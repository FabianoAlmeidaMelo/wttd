from django.test import TestCase

class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / mest return status code 200"""
        # response = self.client.get('/')
        return self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Must usse index.html"""
        # response = self.client.get('/')
        self.assertTemplateUsed(self.response, 'index.html')
