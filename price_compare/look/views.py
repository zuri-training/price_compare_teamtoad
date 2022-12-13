from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from bs4 import BeautifulSoup
import requests
import time


# Create your views here.
from .form import CreateUserForm
from .models import *

def SignUp(request):
    if request.user.is_authenticated:
        return redirect('home')
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

def LogIn(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "username or password is incorrect")
        context={}
        return render(request, 'pages/login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('login')


def Index(request):
    return render(request, "pages/index.html")


def Products (request):
    products=Product.objects.all()
    context={"products":products }
    return render(request, "pages/products.html",context)

@login_required(login_url='login')
def About (request):
    return render(request, "pages/about.html")  


@login_required(login_url='login')
def Documentation (request):
    return render(request, "pages/docs.html")


@login_required(login_url='login')
def ProductDetail (request,id, user_id):
    duck={}

    duct=Product.objects.get(id=id)
    user_comments=Comments.objects.filter(product_id=id)
    customers=UserPlus.objects.get(id=user_id)

    product_kara=duct.url_kara
    product_kon=duct.url_konga
    product_jumia=duct.url_jumia
    duck["name"]=duct.product_name
    try:
        ka_result=requests.get(product_kara) # type: ignore #i
        doc=BeautifulSoup(ka_result.text,"html.parser")
    
        # PRICE KARA
        span=doc.find(["span"],class_="price")
        price=str(span).split(">")[-2].strip("<span class="">/ price NGN")
        kara_price=price.strip(",")[1:]
        if kara_price == "":
            duck["image"]="Image removed"
        else:
            duck["priceKara"]=kara_price

        # # IMAGE KARA
        img=doc.find_all(["img"],alt="main product photo")
        imageKara=str(img).split("=")[4][1:-4]

        url = imageKara
        response = requests.get(url)
        duck["image"]=response.url
    except:
        duck["image"]="Image removed"


    try:
        kon_result=requests.get(product_kon) # type: ignore #i
        salt=BeautifulSoup(kon_result.text,"html.parser")

        # # PRICE KONGA
        div=salt.find(["div"],class_="_678e4_e6nqh")
        priceKonga=div.contents[1] # type: ignore #i
        duck["priceKonga"]=priceKonga
    except :
        duck["priceKonga"]="Price removed"



    try:
        jumia_result=requests.get(product_jumia) # type: ignore #i
        gum=BeautifulSoup(jumia_result.text,"html.parser")
        # # PRICE JUMIA
        jum_span=gum.find(["span"],class_="-b -ltr -tal -fs24")
        # print(jum_span)
        priceJumia=str(jum_span).split(">")[1].strip("</span ₦")
        # print(priceJumia)
        duck["priceJumia"]=priceJumia
    except :
        duck["priceJumia"]="Price removed"  
    
    if request.method == "POST":
        comment_plus=request.POST.get('comments')
        while comment_plus == "":
            messages.info(request, "comments cannot be empty")
            break
        else:
            if comment_plus != "":
                comment=Comments(comments=comment_plus,customer_id=customers, product_id=duct)
                comment.save()
                messages.success(request, "comments successfully added")
        
    context={"data":duck, "comments":user_comments}
    return render(request, "pages/productDetail.html",context) 

@login_required(login_url='login')
def Profile (request):
    return render(request, "pages/profile.html")
