from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "pages/index.html")

def signup (request):
    return render(request, "pages/signup.html")

def login (request):
    return render(request, "pages/login.html")

def about (request):
    return render(request, "pages/about.html")  

def docs (request):
    return render(request, "pages/docs.html")

def products (request):
    return render(request, "pages/products.html")

def productDetail (request):
    return render(request, "pages/productDetail.html") 

