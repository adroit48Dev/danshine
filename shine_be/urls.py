"""
URL configuration for shine_be project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import pastepper_formth, include, re_path
from django.conf.urls.i18n import i18n_patterns
from ..s_members.urls import *

import shine_be.settings as settings
from django.conf.urls.static import static

# urlpatterns = [ i18n_patterns(
#     re_path(r'^shine-management/', admin.site.urls, name='admin'),
#     path('shine-management/clearcache/', include('clearcache.urls')),
# )

# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path("admin/", admin.site.urls),
    path("admin/")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
