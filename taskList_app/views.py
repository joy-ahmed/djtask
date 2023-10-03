from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import ProfileImg
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
    avatar = None
    try:
        avatar = ProfileImg.objects.get(user=request.user).profileImg
    except:
        avatar = ""

    return render(request, 'home.html', {"avatar": avatar})


def howitworks(request):
    avatar = None
    try:
        avatar = ProfileImg.objects.get(user=request.user).profileImg.url
    except:
        avatar = ""
    return render(request, 'howitworks.html', {"avatar": avatar})


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        print(username, password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("all-task")
    return render(request, 'login.html')


def logoutPage(request):
    logout(request)
    return redirect('login')


def signupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password_one = request.POST.get("password_one")
        password_two = request.POST.get("password_two")
        avatar = request.FILES["avatar"]
        if password_one == password_two:
            user = User(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = make_password(password_one),
            )
            user.save()

            user_avatar = ProfileImg(
                profileImg = avatar,
                user = user
            )

            user_avatar.save()

            return redirect("login")
        else:
            return redirect('signup')
    return render(request, 'signup.html')




def allTasks(request):
    avatar = None
    try:
        avatar = ProfileImg.objects.get(user=request.user).profileImg.url
    except:
        avatar = ""
    return render(request, "tasklist.html", {"avatar": avatar})