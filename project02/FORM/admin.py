from django.contrib import admin
# from django.contrib.admin.sites import site
from FORM.models import formclass

# Register your models here.

class formadmin(admin.ModelAdmin):
    list_display=("name","email","phone","website","message")


admin.site.register(formclass,formadmin)
