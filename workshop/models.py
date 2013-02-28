# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
import datetime


class Part_Types(models.Model):
	name = models.CharField(max_length=30, 
							verbose_name=u'Наименование типа детали',
							help_text = u'Детали из которых состоит аппарат')
	class Meta:
		verbose_name = (u'Вид детали')
    	verbose_name_plural = (u'Виды деталей')	
	def __unicode__(self):
		return (self.name)


class Part_Operations_Types(models.Model):
	part_type = models.ForeignKey(Part_Types, verbose_name=u'тип детали')
	name = models.CharField(max_length=30, verbose_name=u'вид ремонта')
	
	class Meta:
		verbose_name = (u'Вид операции')
    	verbose_name_plural = (u'Виды операций')	

	def __unicode__(self):
		return (self.name)
	
class Parts(models.Model):
	number = models.CharField(max_length=3, verbose_name=u'номер')
	part_type = models.ForeignKey(Part_Types, verbose_name=u'тип детали')
	create_date = models.DateTimeField(verbose_name=u'дата начала эксплуатации', 
										auto_now_add=True)
	last_modify_date = models.DateTimeField(verbose_name=u'дата последней операции', 
											auto_now=True)
	comment = models.TextField(verbose_name=u'примечание', blank=True, null=True)

	class Meta:
#		verbose_name = (u'Деталь')
#		verbose_name_plural = (u'Детали')	
		ordering = ['-last_modify_date']
		unique_together = (('number', 'part_type'),)

	def __unicode__(self):
		return '%s %s %s %s' % (unicode(self.part_type), self.number, 
			self.last_modify_date.strftime("%d.%m.%y %H:%M"), 
			self.create_date.strftime("%d.%m.%y %H:%M"))
								


class Part_Operations(models.Model):
	part = models.ForeignKey(Parts, verbose_name=u'Деталь')
	operation = models.ForeignKey(Part_Operations_Types, verbose_name=u'Вид ремонта')
	op_date = models.DateTimeField(verbose_name=u'Дата операции', default=datetime.datetime.now)
	op_master = models.ForeignKey(User)
	comment = models.TextField(blank=True, null=True, verbose_name=u'Примечание')

	class Meta:
		verbose_name = (u'Ремонт')  
    	verbose_name_plural = (u'Ремонты')	

	def __unicode__(self):
		return '%s %s' % (self.part, self.operation)