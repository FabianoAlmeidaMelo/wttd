from django.test import TestCase
from django.shortcuts import resolve_url
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact, Course, Talk

class TalkListGet(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(
                                        name = 'Alan Turing',
                                        slug = 'alan-turing',
                                        photo = 'http://hbn.link/turing-pic',
                                        site = 'http://hbn.link/turing-site',
                                        description = 'Matemático e decifrador de códigos.',
                                    )
        t1 = Talk.objects.create(title = 'Título da Palestra',
                            start = '10:00',
                            description = 'Descrição da Palestra')
        t2 = Talk.objects.create(title = 'Título da Palestra',
                            start = '13:00',
                            description = 'Descrição da Palestra')
        c1 = Course.objects.create(title = 'Título do Curso',
                            start = '09:00',
                            description = 'Descrição do curso',
                            slots=20)
        t1.speakers.add(speaker)
        t2.speakers.add(speaker)
        c1.speakers.add(speaker)
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
                    (3, '/palestrantes/alan-turing/'),
                    (3, 'Alan Turing'),
                    (2, 'Descrição da Palestra'),
                    (1, 'Título do Curso'),
                    (1, 'Descrição do curso'),
                    (1, '09:00'),
                    ]
        with self.subTest():
            for count, expected in contents:
                self.assertContains(self.response, expected, count)

class TalkListEmpty(TestCase):
    def test_get_empty(self):
        response = self.client.get(resolve_url('talk_list'))
        self.assertContains(response, 'Ainda não existem palestras de manhã')
        self.assertContains(response, 'Ainda não existem palestras de tarde')
