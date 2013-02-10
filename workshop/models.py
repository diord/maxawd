# coding: utf-8
from django.db import models
import datetime

class Part_Types(models.Model):
	name = models.CharField(max_length=30, verbose_name="наименование типа детали",
							help_text = 'Детали из которых состоит аппарат')
	
	def __unicode__(self):
		return self.name

class Part_Operations_Types(models.Model):
	part_type = models.ForeignKey(Part_Types, verbose_name='тип детали')
	name = models.CharField(max_length=30, verbose_name='вид ремонта')
	
	def __unicode__(self):
		return self.name

class Parts(models.Model):
	number = models.CharField(max_length=3, verbose_name='номер')
	part_type = models.ForeignKey(Part_Types, verbose_name='тип детали')
	create_date = models.DateTimeField(verbose_name='дата начала эксплуатации', 
										auto_now_add=True)
	last_modify_date = models.DateTimeField(verbose_name='дата последней операции', 
											auto_now=True)
	comment = models.TextField(verbose_name="примечание", blank=True, null=True)
	class Meta:
		ordering = ['-last_modify_date']
        verbose_name = 'Drive leg'
        verbose_name_plural = '!!!'

	def __unicode__(self):
		return u'%s №%s (последняя операция %s / начало эксплуатации %s)' % (self.part_type, self.number, 
									self.last_modify_date.strftime("%d.%m.%y %H:%M"),
									self.create_date.strftime("%d.%m.%y %H:%M"))

#	class Meta:
#    	ordering = ["last_modify_date"]
class Part_Operations(models.Model):
	part = models.ForeignKey(Parts, verbose_name='деталь')
	operation = models.ForeignKey(Part_Operations_Types, verbose_name='вид ремонта')
	op_date = models.DateTimeField(verbose_name='дата операции')
	op_master = models.CharField(max_length=30, verbose_name='мастер')
	comment = models.TextField(blank=True, null=True, verbose_name='примечание')

	def __unicode__(self):
		return '%s %s' % (self.part, self.operation)