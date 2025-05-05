from django.contrib import admin
from .models import User

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password',)
    search_fields = ('id', 'name', 'email',)

# admin.site.register(User, UserAdmin)

