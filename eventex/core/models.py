from django.db import models
from django.shortcuts import resolve_url
from eventex.core.managers import KindQuerySet, PeriodManger

class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.CharField('slug', max_length=50)
    photo = models.URLField('foto')
    site = models.URLField('website',  blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return resolve_url('speaker_detail', slug=self.slug)

class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'email'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', verbose_name='palestrante')
    kind = models.CharField('tipo', max_length=1, choices=KINDS)
    value = models.CharField('valor', max_length=255)

    objects = KindQuerySet.as_manager()


    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'

    def __str__(self):
        return self.value


class Talk(models.Model):
    title = models.CharField('título', max_length=200)
    start = models.TimeField('início', null=True, blank=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManger()

    class Meta:
        ordering = ['start']
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title


class Course(Talk):
    slots = models.IntegerField()

    objects = PeriodManger()

    class Meta:
        verbose_name = 'curso'
        verbose_name_plural = 'cursos'
