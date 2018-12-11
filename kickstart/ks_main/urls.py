from django.urls import path, re_path, include
from .views import home, home_files

urlpatterns = [
    path('', home, name='home'),
    re_path(r'^(?P<filename>(robots.txt)|(humans.txt))$', home_files, name='home-files'),
]
