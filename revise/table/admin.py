from django.contrib import admin
from table.models import Info

# Register your models here.
@admin.register(Info)

class AdminInfo(admin.ModelAdmin):
    list_display=("id","name","password")
