from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
from .form import CreateUserForm
from .models import *

def SignUp(request):
    if request.user.is_authenticated:
        return reverse(redirect('look:home'))
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request, "Account was created for" + user)
                return redirect("login")
        context ={"form":form}
        return render(request, "pages/signup.html", context)

# def signup (request):
#     return render(request, "pages/signup.html")
def LogIn(request):
    if request.user.is_authenticated:
        return redirect(reverse('look:home'))
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('look:home'))
            else:
                messages.info(request, "username or password is incorrect")
        context={}
        return render(request, 'registration/login.html', context)

def LogoutUser(request):
    logout(request)
    return render(request)


def Index(request):
    return render(request, "pages/index.html")


def Products (request):
    return render(request, "pages/products.html")

@login_required(login_url='login')
def About (request):
    return render(request, "pages/about.html")  


@login_required(login_url='login')
def Documentation (request):
    return render(request, "pages/docs.html")


@login_required(login_url='login')
def ProductDetail (request):
    return render(request, "pages/productDetail.html") 

@login_required(login_url='login')
def Profile (request):
    return render(request, "pages/profile.html")
