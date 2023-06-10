from typing import List
from django.contrib import admin
from django.apps import apps
from django.urls.resolvers import URLResolver
from s_members.models import *
from django.urls import path, re_path
from django.http import HttpResponse
from s_members.views import *

# from .views import upload_data


# register site

admin.site.register(Member)

admin.site.register(MemberAddress)
admin.site.register(Education)
admin.site.register(MemberEducation)
admin.site.register(Occupation)
admin.site.register(MemberOccupation)
admin.site.register(MemberRegistration)

class CustomAdminSite(admin.AdminSite):
    
    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            re_path(r'members/bulk_upload$', self.admin_view()),
            re_path(r'members/create$',  member_create()),
        ]