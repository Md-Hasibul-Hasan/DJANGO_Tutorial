from django.contrib import admin
from userform.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')  # Fields to display in the admin list view
    search_fields = ('id', 'name', 'email')  # Fields to enable search in the admin interface

# # admin.site.register(User, UserAdmin)
