from django.contrib import admin

from users.models import User

# Register your models here.
# admin.site.register

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'is_staff']