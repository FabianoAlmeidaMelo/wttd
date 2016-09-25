from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """ Form must have 4 fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        '''cpf só contém números'''
        form = self.make_validate_form(cpf='1ABC5678901')
        field = 'cpf'
        code = 'digits'
        # self.assertFormMessage(form, field, msg)
        self.assertFormErrorCode(form, field, code)

    def test_cpf_has_11_digit(self):
        '''cpf 11 digitos'''
        form = self.make_validate_form(cpf='1234')
        # msg = 'CPF deve ter apenas 11 dígitos'
        field = 'cpf'
        # self.assertFormMessage(form, field, msg)
        code = 'length'
        self.assertFormErrorCode(form, field, code)

    def test_name_must_be_capitalized(self):
        """1ª Letra Maiuscula o resto minúscula"""
        # FABIANO melo --> Fabiano Melo
        form = self.make_validate_form(name='FABIANO melo')
        self.assertEqual('Fabiano Melo', form.cleaned_data['name'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validate_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validate_form(phone='')
        self.assertFalse(form.errors)

    def test_must_informe_email_or_phone(self):
        form = self.make_validate_form(phone='', email='')
        self.assertListEqual(['__all__'], list(form.errors))

    def assertFormMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]

        self.assertListEqual([msg], errors_list)

    def make_validate_form(self, **kwargs):
        valid = dict(name='Fabiano Almeida',
                     cpf='12345678901',
                     email='email@uol.com',
                     phone='12-982239764')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
