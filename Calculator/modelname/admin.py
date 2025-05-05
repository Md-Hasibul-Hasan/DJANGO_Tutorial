from django.contrib import admin
from modelname.models import modelclass

# Register your models here.
class modeladmin(admin.ModelAdmin):

    list_display=("icon","title","description")

admin.site.register(modelclass,modeladmin)

