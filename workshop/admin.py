# -*- coding: utf-8 -*- 
from django.contrib import admin
from django.template import RequestContext
from workshop.models import Money, Payments_History, Part_Types, Part_Operations_Types, Parts, Part_Operations, ClientsPlaces

class Part_Types_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Parts_Admin(admin.ModelAdmin):
	list_filter = ('part_type',)
	date_hierarchy = 'last_modify_date'
	
class Part_Operations_Admin(admin.ModelAdmin):
    list_display = ('part', 'operation', 'op_date', 'op_master')
    def save_model(self, request, obj, form, change):
        obj.op_master = request.user 
        obj.save()
        super(Part_Operations_Admin, self).save_model(request, obj, form, change)    

class ClientsPlaces_Admin (admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)    

class Payments_History_Admin(admin.ModelAdmin):
    list_display = ('Client',)


admin.site.register(Part_Types,             Part_Types_Admin        )
admin.site.register(Part_Operations_Types                           )
admin.site.register(Parts,                  Parts_Admin             )
admin.site.register(Part_Operations,        Part_Operations_Admin   )
admin.site.register(ClientsPlaces,          ClientsPlaces_Admin     )
admin.site.register(Payments_History, Payments_History_Admin)
admin.site.register(Money  )


