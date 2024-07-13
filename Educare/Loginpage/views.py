from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from Students.models import Student  # Assuming these are your models
# from Teachers.models import Achievement
# from Event.models import Event
import datetime

# Home page view with login required decorator
@login_required(login_url='login')
def HomePage(request):
    username = request.user.username  # Access the username
    return render(request, 'Loginpage/home.html', {'username': username})

# Signup page view
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        print(uname, email, pass1, pass2)

        if User.objects.filter(username=uname).exists():
            return HttpResponse("Username already exists. Please choose a different username.")

        # Check if passwords match
        if pass1 != pass2:
            return HttpResponse("Passwords do not match. Please try again.")
        else:
            # Create a new user
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'Loginpage/signup.html')

# Login page view
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")

    return render(request, 'Loginpage/login.html')

# Faculty login page view
def faculty_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect")

    return render(request, 'Loginpage/faculty_loginpage.html')

# Logout page view
def LogoutPage(request):
    logout(request)
    return redirect('login')

# Home view with student information
@login_required(login_url='login')
def home(request):
    student = Student.objects.get(user=request.user)
    top_students = Student.objects.order_by('-total_marks')[:3]
    top_10_students = Student.objects.order_by('-total_marks')[:10]
    achievements = Achievement.objects.all()
    events = Event.objects.filter(date__gte=datetime.date.today())

    context = {
        'student': student,
        'top_students': top_students,
        'top_10_students': top_10_students,
        'achievements': achievements,
        'events': events
    }
    return render(request, 'landing_page.html', context)
