from django.contrib import admin

# Register your models here.
from projectapp.models import StudentQuestion
admin.site.register(StudentQuestion)





from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

class CustomUserAdmin(DefaultUserAdmin):
    model = User

    # Customizing the fieldsets for the change form
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Customizing the add_fieldsets for the creation form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

# Unregister the default User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)





from projectapp.models import TeachersAnwser
admin.site.register(TeachersAnwser)
