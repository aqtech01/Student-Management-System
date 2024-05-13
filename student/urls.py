from django.urls import path
from student.views import *

urlpatterns = [    
    path("", home, name="home"),
]
