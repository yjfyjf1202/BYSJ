from django.conf.urls import url

from .views import *



urlpatterns = [
    url(r'getLYRCJob',getLYRCJob),
    url(r'screenInfo',screenInfo)
]