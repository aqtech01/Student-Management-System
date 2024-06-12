from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import StudentForm


# Create your views here.#

def home(request):
    student = Student.objects.all()
    context = {
        "student": student,
        "title": "Home"
    }
    return render(request, "student/index.html", context)


def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse("home"))


def add(request):
    if request.method == "POST":
        new_student_no = request.POST.get("student_no")
        new_student_first_name = request.POST.get("first_name")
        new_student_last_name = request.POST.get("last_name")
        new_student_email = request.POST.get("email")
        new_student_field_of_study = request.POST.get("field_of_study")
        new_student_cgpa = request.POST.get("cgpa")

        new_student = Student(
            student_no=new_student_no,
            first_name=new_student_first_name,
            last_name=new_student_last_name,
            email=new_student_email,
            field_of_study=new_student_field_of_study,
            cgpa=new_student_cgpa
        )
        new_student.save()
        return redirect("home")
    else:
        context = {
            "title": "Add Students"
        }
        return render(request, "student/add.html", context)


def edit(request, id):
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return HttpResponseNotFound("Student not found")

    if request.method == "POST":
        try:
            student.student_no = request.POST.get("student_no")
            student.first_name = request.POST.get("first_name")
            student.last_name = request.POST.get("last_name")
            student.email = request.POST.get("email")
            student.field_of_study = request.POST.get("field_of_study")
            student.cgpa = request.POST.get("cgpa")
            # ... and so on for other fields
            student.save()
            return redirect("home")
        except ValidationError as e:  # type: ignore
            # Handle form validation errors here
            context = {
                "error": "An error occurred. Please check your data.",
                "student": student,
                "errors": e.message_dict}  # Include specific error messages
            return render(request, "student/edit.html", context)
    else:
        context = {"student": student}
        return render(request, "student/edit.html", context)


def delete(request, id):
    try:
        student = Student.objects.get(pk=id)
        student.delete(),
        messages.success(request, "Student Deleted Successful")
    except Student.DoesNotExist:
        messages.success(request, "Student Doesn't Found")
    return redirect("home")
