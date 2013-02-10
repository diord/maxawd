from django.contrib import admin
from workshop.models import Part_Types, Part_Operations_Types, Parts, Part_Operations

class Part_Types_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class Parts_Admin(admin.ModelAdmin):
	list_filter = ('part_type',)
	date_hierarchy = 'last_modify_date'
	
admin.site.register(Part_Types, Part_Types_Admin)
admin.site.register(Part_Operations_Types)
admin.site.register(Parts, Parts_Admin)
admin.site.register(Part_Operations)
