from django.urls import path
from . import RequestProcess

urlpatterns = [

    path('request', RequestProcess.testrequest)
]