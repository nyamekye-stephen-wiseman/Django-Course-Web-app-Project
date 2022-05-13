from doctest import debug_script
import re
from django.shortcuts import redirect, render
from . models import Profile
from django.contrib.auth.models import User
from . forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def loginUser(request):

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")

        user = authenticate(request, username=username, password=password) 

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, "Invalid credentials")
               

    return render(request, 'users/login-register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "You are logged out")
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            messages.success(request, 'Registration sucessfully completed.')
            return redirect("profiles")


    context = {'page':page, 'form':form}
    return render(request, 'users/login-register.html', context)

def profiles(request):
    profiles = Profile.objects.all()
    context = {
        'profiles':profiles,
    }
    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        "profile":profile,
        "topSkills":topSkills,
        "otherSkills":otherSkills,
    }
    return render(request, 'users/user-profile.html', context)
