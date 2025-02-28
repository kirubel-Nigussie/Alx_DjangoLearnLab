from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """Customize the Django admin panel for the CustomUser model."""
    
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "date_of_birth", "profile_photo", "password1", "password2", "is_active", "is_staff", "is_superuser"),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")

admin.site.register(CustomUser, CustomUserAdmin)

