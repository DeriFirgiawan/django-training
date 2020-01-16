from django.contrib import admin
from .models import DataForm
# Register your models here.
class DataAdmin(admin.ModelAdmin):
	readonly_fields = [
		'slug',
		'published',
		'updated',
	]

admin.site.register(DataForm,DataAdmin)