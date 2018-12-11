# -*- coding: utf-8 -*-
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.i18n import i18n_patterns
from ks_main.views import home_files

urlpatterns = [
    re_path(r'^(?P<filename>(robots.txt)|(humans.txt))$',
        home_files, name='home-files'),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('ks_main.urls')),
)
