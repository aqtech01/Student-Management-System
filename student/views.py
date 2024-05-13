from django.shortcuts import render
from .models import *

# Create your views here.#

def home(request):
    student = Student.objects.all()
    context = {
        "student" : student,
        "title":"Home"
    }
    return render(request, "student/index.html",context)
