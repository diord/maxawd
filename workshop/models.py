from django.db import models


class Part_Types(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name

class Part_Operations_Types(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name

class Parts(models.Model):
	number = models.CharField(max_length=3)
	part_type = models.ForeignKey(Part_Types)
	create_date = models.DateTimeField()
	last_modify_date = models.DateTimeField()
	
	def __unicode__(self):
		return '%s %s %s' % (self.number, self.last_modify_date, self.create_date)

class Part_Operations(models.Model):
	part = models.CharField(max_length=30)
	operation = models.ForeignKey(Part_Operations_Types)
	op_date = models.DateTimeField()
	op_master = models.CharField(max_length=30)
	op_description = models.CharField(max_length=255)

	def __unicode__(self):
		return '%s %s' % (self.part, self.operation)
