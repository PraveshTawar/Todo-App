from django.contrib import admin
from .models import todolist

# Register your models here.
class todoAdmin(admin.ModelAdmin):
    list_display = [ "task","user"]

# admin.site.register(todolist)
admin.site.register(todolist,todoAdmin)

