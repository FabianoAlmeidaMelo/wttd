from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscribeGet(TestCase):
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
        tags =(('<form', 1),
               ('<input', 6),
               ('type="text"', 3),
               ('type="email"', 1),
               ('type="submit"', 1),
            )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)
        # self.assertContains(self.response, '<form')
        # self.assertContains(self.response, '<input', 6) #nome, cpf, email, tele, submit, token
        # self.assertContains(self.response, 'type="text"', 3) #nome, cpf, telefone
        # self.assertContains(self.response, 'type="email"')
        # self.assertContains(self.response, 'type="submit"')

    def test_csrf(self):
        """4: Html must contain csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """5: Html must have subscription form"""
        # form = self.response.context['form']
        self.assertIsInstance(self.form, SubscriptionForm)


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name="Fabiano Almeida", cpf='12345678901',
                    email='falmeidamelo@uol.com.br', phone='12-98223-9764')
        self.response = self.client.post('/inscricao/', data)

    def test_post(self):
        """1: valid POST should redirect to/inscricao/"""
        self.assertEqual(302, self.response.status_code)

    def test_send_subscribe_email(self):
        """2: must count email"""
        self.assertEqual(1, len(mail.outbox))


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.response = self.client.post('/inscricao/', {'name': 'Fabiano', 'phone': '1', 'email': 'hkj'})
        self.form = self.response.context['form']
        # print('ERROS: ', self.form.errors)
        # informe um endereço de email válido

    def test_post(self):
        """Invalid POST should not redirect"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        """Html must have subscription form"""
        # form = self.response.context['form']
        self.assertIsInstance(self.form, SubscriptionForm)

    def test_form_has_errors(self):
        self.assertTrue(self.form.errors)


class SubscribeSuccsesMessage(TestCase):
    def setUp(self):
        data = dict(name="Fabiano Almeida", cpf='12345678901',
                    email='falmeidamelo@uol.com.br', phone='12-98223-9764')
        self.response = self.client.post('/inscricao/', data, follow=True)
        # follow True, vai seguir o redirect

    def test_message(self):
        self.assertContains(self.response, 'Inscrição realizada com sucesso!')