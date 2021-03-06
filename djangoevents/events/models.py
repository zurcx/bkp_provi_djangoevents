# encoding: utf-8

from django.db import models
from  django.core.urlresolvers import reverse

class Event(models.Model):

	TYPE_CHOICES = (
	(1, u'Workshop'),
	(2, u'Dojo'),
	(3, u'Palestra'),
	)

	name = models.CharField(verbose_name=u"Nome",
					 	    max_length=100)
	type = models.IntegerField(choices=TYPE_CHOICES,
		                       verbose_name=u'Tipo de Evento')
	description = models.TextField(verbose_name=u'Descrição',
									blank=True)
	created_on = models.DateTimeField(verbose_name='Criado em ',
									  auto_now_add=True)
	link = models.URLField(verbose_name='Link', blank=True)
	public = models.BooleanField(verbose_name='Publíco?', default=True)

	def comments_count(self):
		return self.comments.count()
	comments_count.short_description = u'Número de comentários'

	@models.permalink
	def get_absolute_url(self):
		return ('events_details', (), {'pk':self.pk})


	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Evento'
		verbose_name_plural = u'Eventos'
		ordering = ['name']

class Comment(models.Model):

	name = models.CharField(verbose_name=u'Nome',
							max_length=100)
	email = models.EmailField(verbose_name='E-mail',)
	event = models.ForeignKey(Event, verbose_name='Evento',
		                      related_name='comments')
	text = models.TextField(verbose_name=u'Texto')
	website =  models.URLField(verbose_name=u'Website', blank=True)
	created_on = models.DateTimeField(verbose_name=u'Criado em',
									  auto_now_add=True)

	def __unicode__(self):
		return self.text

	class Meta:
		verbose_name = u'Comentário'
		verbose_name_plural =  u'Comentários'
		ordering = ['created_on']

