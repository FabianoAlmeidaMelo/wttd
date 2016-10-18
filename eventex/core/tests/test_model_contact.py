from django.test import TestCase
from django.shortcuts import resolve_url
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact

class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
                                        name = 'Grace Hopper',
                                        slug = 'grace-hopper',
                                        photo = 'http://hbn.link/hopper-pic',
                                        site = 'http://hbn.link/hopper-site',
                                        description = 'Programadora e almirante.',
                                    )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.EMAIL,
                                         value='fabiano@znc.com.br')
        self.assertTrue(Speaker.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind=Contact.PHONE,
                                         value='12-33334567')
        self.assertTrue(Speaker.objects.exists())


    def test_choices(self):
        '''Kind: E or P'''
        contact = Contact.objects.create(speaker=self.speaker,
                                         kind='A',
                                         value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact.objects.create(speaker=self.speaker,
                                 kind=Contact.PHONE,
                                 value='12-33334567')
        self.assertEqual('12-33334567', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
                                    name = 'Grace Hopper',
                                    slug = 'grace-hopper',
                                    photo = 'http://hbn.link/hopper-pic',
                                    site = 'http://hbn.link/hopper-site',
                                    description = 'Programadora e almirante.',
                                )
        s.contact_set.create(kind=Contact.EMAIL, value='hopper@grace.com')
        s.contact_set.create(kind=Contact.PHONE, value='12-95678123')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['hopper@grace.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['12-95678123']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
