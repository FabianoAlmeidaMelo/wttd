from django.test import TestCase
from django.shortcuts import resolve_url
from eventex.core.models import Speaker, Talk

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk=Talk.objects.create(
                            title = 'Título da Palestra',
                            start = '10:00',
                            description = 'Descrição da Palestra',
                        )


    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk has many Speaker and vice versa"""
        self.talk.speakers.create(
            name='Alan Turin',
            slug='alan-turin',
            site='http://hbn.link/turin-site'
            )
        self.assertEqual(1, self.talk.speakers.count())

    def test_descriptiom_can_be_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_can_be_blank(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_can_be_blank(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_can_be_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra', str(self.talk))
