# -*- coding: utf-8 -*- 
from django.db import models
from django.contrib.auth.models import User
import datetime


class Part_Types(models.Model):
	name = models.CharField(max_length=30, 
							verbose_name="наименование типа детали",
							help_text = u'Детали из которых состоит аппарат')
	class Meta:
		verbose_name = (u'Вид детали')
    	verbose_name_plural = (u'Виды деталей')	
	def __unicode__(self):
		return unicode(self.name)


class Part_Operations_Types(models.Model):
	part_type = models.ForeignKey(Part_Types, verbose_name=u'тип детали')
	name = models.CharField(max_length=30, verbose_name=u'вид ремонта')
	
	class Meta:
		verbose_name = (u'Вид операции')
    	verbose_name_plural = (u'Виды операций')	

	def __unicode__(self):
		return unicode(self.name)
	
class Parts(models.Model):
	number = models.CharField(max_length=3, verbose_name=u'номер')
	part_type = models.ForeignKey(Part_Types, verbose_name=u'тип детали')
	create_date = models.DateTimeField(verbose_name=u'дата начала эксплуатации', 
										auto_now_add=True)
	last_modify_date = models.DateTimeField(verbose_name=u'дата последней операции', 
											auto_now=True)
	comment = models.TextField(verbose_name=u"примечание", blank=True, null=True)

	def __unicode__(self):
		return '%s %s %s %s' % (self.part_type, self.number, 
									self.last_modify_date.strftime("%d.%m.%y %H:%M"),
									self.create_date.strftime("%d.%m.%y %H:%M"))
 	class Meta:
#		verbose_name = (u'Деталь')
#		verbose_name_plural = (u'Детали')	
		ordering = ['-last_modify_date']
		unique_together = (('number', 'part_type'),)


class Part_Operations(models.Model):
	part = models.ForeignKey(Parts, verbose_name=u'detal')
	operation = models.ForeignKey(Part_Operations_Types, verbose_name=u'vid remonta')
	op_date = models.DateTimeField(verbose_name=u'dataop', default=datetime.datetime.now)
	op_master = models.ForeignKey(User)
	comment = models.TextField(blank=True, null=True, verbose_name=u'prim')

	class Meta:
		verbose_name = (u'remont')  
    	verbose_name_plural = (u'remonty')	

	def __unicode__(self):
		return '%s %s' % self.part, self.operation