from django.test import TestCase
from django.shortcuts import resolve_url
from eventex.core.models import Course, Speaker, Talk
from eventex.core.managers import PeriodManger


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


class PeriodmangerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start='11:59')
        Talk.objects.create(title='Afternoom Talk', start='12:00')

    def test_manger(self):
        self.assertIsInstance(Talk.objects, PeriodManger)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['Morning Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ['Afternoom Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)


class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Título do Curso',
            description='Descrição do curso',
            start='09:00',
            slots=20,
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())

    def test_speaker(self):
        """Course has many speakers and vice -versa"""
        self.course.speakers.create(
            name='Alan Turin',
            slug='alan-turin',
            site='http://hbn.link/turin-site'
        )
        self.assertEqual(1, self.course.speakers.count())

    def test_str(self):
        self.assertEqual('Título do Curso', str(self.course))

    def test_manger(self):
        self.assertIsInstance(Course.objects, PeriodManger)
