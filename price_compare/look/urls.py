from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home" ),
    path('login/', login, name="login"),
    path('signup/', signup, name="signup" ),
    path('products/', products, name="products"),
    path('productDetail/', productDetail, name="productDetail"),
    path('about/', about, name="about"),
    path('docs/', docs, name="docs")

]