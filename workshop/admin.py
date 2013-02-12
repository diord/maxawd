from django.contrib import admin
from django.template import RequestContext
from workshop.models import Part_Types, Part_Operations_Types, Parts, Part_Operations

class Part_Types_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Parts_Admin(admin.ModelAdmin):
	list_filter = ('part_type',)
	date_hierarchy = 'last_modify_date'
	
class Part_Operations_Admin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user 
       	obj.save()

class DocumentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.last_modified_by = request.user
        obj.save()

admin.site.register(Part_Types, Part_Types_Admin)
admin.site.register(Part_Operations_Types)
admin.site.register(Parts, Parts_Admin)
admin.site.register(Part_Operations, Part_Operations_Admin)