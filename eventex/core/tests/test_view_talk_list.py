from django.test import TestCase
from django.shortcuts import resolve_url
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact, Talk

class TalkListGet(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
                                        name = 'Alan Turin',
                                        slug = 'alan-turin',
                                        photo = 'http://hbn.link/turin-pic',
                                        site = 'http://hbn.link/turin-site',
                                        description = 'Matemático e decifrador de códigos.',
                                    )
        t1 = Talk.objects.create(title = 'Título da Palestra',
                            start = '10:00',
                            description = 'Descrição da Palestra')
        t2 = Talk.objects.create(title = 'Título da Palestra',
                            start = '13:00',
                            description = 'Descrição da Palestra')
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        self.response = self.client.get(resolve_url('talk_list'))

    def test_get(self):
        """1: GET /detail/ must return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """2: Must use core/talk_list.html"""
        self.assertTemplateUsed(self.response, 'core/talk_list.html')

    def test_context(self):
        variables = ['morning_talks', 'afternoon_talks']
        for key in variables:
            with self.subTest():
                self.assertIn(key, self.response.context)

#     def test_context(self):
#         subscription = self.response.context['subscription']
#         self.assertIsInstance(subscription, Subscription)


    def test_html(self):
        contents = [
                    (2, 'Título da Palestra'),
                    (1, '10:00'),
                    (1, '13:00'),
                    (2, '/palestrantes/alan-turin/'),
                    (2, 'Alan Turin'),
                    (2, 'Descrição da Palestra'),
                    ]
        with self.subTest():
            for count, expected in contents:
                self.assertContains(self.response, expected, count)

class TalkListEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(resolve_url('talk_list'))
        self.assertContains(response, 'Ainda não existem palestras de manhã')
        self.assertContains(response, 'Ainda não existem palestras de tarde')
