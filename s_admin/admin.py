from django.contrib import admin
from django.apps import apps
from django.contrib.auth.admin import UserAdmin

from s_admin.forms import CustomUserCreationForm, CustomUserChangeForm
from s_admin.models import *

# Register your models here.
    
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    list_select_related = ('user_profile', ) 
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# newModels = apps.get_models()

# admin.site.unregister(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)

admin.site.register(OrganizationSetting)
admin.site.register(Zone)
admin.site.register(Area)
admin.site.register(ZoneGroup)
admin.site.register(Streets)
admin.site.register(FeeSettings)
admin.site.register(RoleSettings)
admin.site.register(PermissionSettings)
# admin.site.register(RolePermissions)


admin.site.site_header = "Shine Co-Operative Society"

# admin.site.site_header = 'Awesome Inc. Administration'
admin.site.site_title = 'Shine Co-Operative Society'