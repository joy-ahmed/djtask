from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def howitworks(request):
    return render(request, 'howitworks.html')


def loginPage(request):
    return render(request, 'login.html')

def signupPage(request):
    return render(request, 'signup.html')