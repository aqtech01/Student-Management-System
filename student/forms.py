from django import forms

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["student_no","first_name","last_name","email","field_of_study","cgpa"]

        labels = {
            "student_no":"Student Number",
            "first_name":"First Name",
            "last_name":"Last Name",
            "email": "Email",
            "field_of_study":"Field of Study",
            "cgpa":"CGPA"
        }
        widgets = {
            "student_no":forms.NumberInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "field_of_study":forms.TextInput(attrs={"class":"form-control"}),
            "cgpa":forms.NumberInput(attrs={"class":"form-control"}),
        }
        