from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/inscricao/')
        self.form = self.response.context['form']

    def test_get(self):
        """1: GET /inscricao/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)
        self.form = self.response.context['form']

    def test_template(self):
        """2: Must use subscription/suscription_form.html"""
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_html(self):
        """3: Html must contain input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 6) #nome, cpf, email, tele, submit, token
        self.assertContains(self.response, 'type="text"', 3) #nome, cpf, telefone
        self.assertContains(self.response, 'type="email"')
        self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """4: Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """5: Html must have subscription form"""
        # form = self.response.context['form']
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_form_has_fields(self):
        """6: Form must have 4 fields"""
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(self.form.fields))
