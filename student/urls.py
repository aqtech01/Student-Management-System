from django.urls import path
from student.views import *

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("<int:id>", view_student, name="view_student"),
    path("add/", add, name="add"),
    path("edit/<int:id>", edit, name="edit"),
    path("delete/<int:id>", delete, name="delete"),
]
