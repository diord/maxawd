# -*- coding: utf-8 -*- 

from django.db import models
from django.contrib.auth.models import User
import datetime
import random

def gen_slug():
    Dt = datetime.datetime.now()
    return u's%04d%02d%02d%02d%02d%02d%03d' % (
        Dt.year, Dt.month, Dt.day,
        Dt.hour, Dt.minute, Dt.second,
        random.randint(0,999))


class ClientsPlaces(models.Model):
    slug        = models.SlugField    ( default         =   gen_slug,
                                        primary_key     =   True)
    name        = models.CharField    ( max_length      =   100, 
                                        verbose_name    =   u'Мойка',
                                        help_text       =   u'Наименование клинингового центра',
                                        blank           =   False, 
                                        null            =   False)
    address     = models.CharField    ( max_length      =   150, 
                                        blank           =   True, 
                                        null            =   True,
                                        verbose_name    =   u'Адрес',
                                        help_text       =   u'Адрес клинингового центра')
    latitude    = models.DecimalField ( max_digits      =   8, 
                                        decimal_places  =   6,
                                        verbose_name    =   u'Широта')
    longitude   = models.DecimalField ( max_digits      =   8,
                                        decimal_places  =   6,
                                        verbose_name    =   u'Долгота')
    worktime    = models.CharField    ( max_length      =   50, 
                                        verbose_name    =   u'Режим работы',
                                        help_text       =   u'Расписание работы клинингового центра',
                                        blank           =   True, 
                                        null            =   True)  
    flag        = models.NullBooleanField ()
    start_date  = models.DateTimeField (verbose_name    =   u'Дата начала работы',
                                        blank           =   True, 
                                        null            =   True, 
                                        auto_now_add    =   False)
    visit_date  = models.DateTimeField (verbose_name    =   u'Дата последнего посещения', 
                                        blank           =   True, 
                                        null            =   True,
                                        auto_now        =   False)
    description = models.TextField     (verbose_name    =   u'Примечание', 
                                        blank           =   True, 
                                        null            =   True)

    class Meta:
        verbose_name        = (u'Мойка')
        verbose_name_plural = (u'Мойки')   
        #ordering            = ['-last_modify_date']

    def __unicode__(self):
        return '%s %s' % (unicode(self.name), 
                          unicode(self.address))

    def get_absolute_url(self):
        return "/maps/%s/" % self.slug


class Part_Types(models.Model):
    name       = models.CharField( max_length      =    30, 
                                   verbose_name    =    u'Наименование типа детали',
                                   help_text       =    u'Детали из которых состоит аппарат')
    class Meta:
        verbose_name        =   (u'Вид детали')
        verbose_name_plural =   (u'Виды деталей') 
    
    def __unicode__(self):
        return (self.name)


class Part_Operations_Types(models.Model):
    part_type   = models.ForeignKey(Part_Types, 
                                    verbose_name    =   u'тип детали')
    name        = models.CharField( max_length      =   30, 
                                    verbose_name    =   u'вид ремонта')
    
    class Meta:
        verbose_name        = (u'Вид операции')
        verbose_name_plural = (u'Виды операций')    

    def __unicode__(self):
        return (self.name)
    
class Parts(models.Model):
    number          = models.CharField      (   max_length      =   3, 
                                                verbose_name    =   u'номер')
    part_type       = models.ForeignKey     (   Part_Types, 
                                                verbose_name    =   u'тип детали')
    create_date     = models.DateTimeField  (   verbose_name    =   u'дата начала эксплуатации', 
                                                auto_now_add=True)
    last_modify_date= models.DateTimeField  (   verbose_name=u'дата последней операции', 
                                                auto_now=True)
    comment         = models.TextField      (   verbose_name=u'примечание', 
                                                blank=True, 
                                                null=True)

    class Meta:
#       verbose_name = (u'Деталь')
#       verbose_name_plural = (u'Детали')   
        ordering        =   ['-last_modify_date']
        unique_together =   (('number', 'part_type'),)

    def __unicode__(self):
        return '%s %s %s %s' % (unicode(self.part_type), 
                                self.number, 
                                self.last_modify_date.strftime  ("%d.%m.%y %H:%M"), 
                                self.create_date.strftime       ("%d.%m.%y %H:%M"))
                                


class Part_Operations(models.Model):
    part            = models.ForeignKey     (   Parts, 
                                                verbose_name=u'Деталь')
    operation       = models.ForeignKey     (   Part_Operations_Types, 
                                                verbose_name=u'Вид ремонта')
    op_date         = models.DateTimeField  (   verbose_name=u'Дата операции', default=datetime.datetime.now)
    op_master       = models.ForeignKey     (   User)
    comment         = models.TextField      (   blank=True, 
                                                null=True, 
                                                verbose_name=u'Примечание')

    class Meta:
        verbose_name        = (u'Ремонт')  
        verbose_name_plural = (u'Ремонты')  

    def __unicode__(self):
        return '%s %s' % (self.part, self.operation)



class Money(models.Model):
    Client          = models.ForeignKey     (   ClientsPlaces, 
                                                verbose_name    =   u'Клиент',
                                                primary_key     =   True)

    Tariff          = models.DecimalField   (   max_digits      =   8, 
                                                decimal_places  =   2,
                                                verbose_name    =   u'Твриф')

    Quant           = models.PositiveSmallIntegerField(   
                                                default         =   1, 
                                                blank           =   False, 
                                                null            =   False)

    Closed_Date      = models.DateTimeField (   verbose_name    =   u'Оплачено до', 
                                                blank           =   True, 
                                                null            =   True,
                                                auto_now        =   False)

    Description     = models.TextField      (   verbose_name    =   u'Примечание', 
                                                blank           =   True, 
                                                null            =   True)

    @property
    def day_credit(self):
        return (Tariff*Quant)

    def __unicode__(self):
        return '%s' % (self.Client)

class Payments_History(models.Model):
    Client          = models.ForeignKey     (   ClientsPlaces, 
                                                verbose_name    =   u'Клиент',
                                                primary_key     =   True)   
    Pay_Date        = models.DateTimeField  (   verbose_name    =   u'Дата оплаты', 
                                                blank           =   True, 
                                                null            =   True,
                                                auto_now        =   False)
    Pay_Sum         = models.DecimalField   (   max_digits      =   8, 
                                                decimal_places  =   2,
                                                verbose_name    =   u'Сумма')
    Description     = models.TextField      (   verbose_name    =   u'Примечание', 
                                                blank           =   True, 
                                                null            =   True)


    def SumOfAllPayments(pClient):
        return (Payments_History.objects.filter(Client=pClient).aggregate(Avg('Pay_Sum')))

    def __unicode_(self):
        return '%s' % (unicode(self.Pay_Sum))
