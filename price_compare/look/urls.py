from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name="home" ),
    path('login/', LogIn, name="login"),
    path('signup/', SignUp, name="signup" ),
    path('logoutUser/', LogoutUser, name="logout"),
    path('products/', Products, name="products"),
    path('productDetail/', ProductDetail, name="productDetail"),
    path('about/', About, name="about"),
    path('docs/', Documentation, name="docs")
    
]