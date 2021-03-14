from sys import path

from django.conf.urls import url

from .views import *



urlpatterns = [

    url(r'getJobList',getJobList),

    # url(r'getDatabaselist',GDBL)
    url(r'inserQCWY',insertQCWY),

    url(r'qcwyScreen',qcwyScreen),
    url(r'ScreenQCWYData',ScreenQCWYData),
    url(r'SearchQCWY',SeacherQCWY)

]
