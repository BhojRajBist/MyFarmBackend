

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User model.
    list_display = ('id', 'email', 'full_name', 'role', 'address', 'is_admin', 'is_active')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name', 'role', 'address')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'role', 'address', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'full_name', 'role', 'address')
    ordering = ('email',)
    filter_horizontal = ()
    radio_fields = {'role': admin.HORIZONTAL}  # Use radio buttons for the 'role' field

# Register the custom User model with the custom UserModelAdmin
admin.site.register(User, UserModelAdmin)

