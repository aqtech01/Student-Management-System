from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def signup_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        confirm_password = data.get("confirm_password")
        if password == confirm_password:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("home")
            except Exception as e:
                messages.error(request, f"something wrong {e}")
        else:
            messages.error(request, "Password and Confirm Password should be same")
            return redirect("signup")

    return render(request, "auth/signup.html")


def signin_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect("signin")

        user = authenticate(username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invaild username or password")
            return redirect("signin")

    return render(request, "auth/signin.html")
