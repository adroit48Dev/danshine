from django.contrib import admin
from s_group.models import *

# Register your models here.
admin.site.register(GroupSetting)
admin.site.register(GroupMembers)
admin.site.register(GroupMemberRole)
admin.site.register(RolePermissions)
