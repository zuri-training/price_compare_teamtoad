from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = "look"

urlpatterns = [
    path('', Index, name="home" ),
    path('login/', LogIn, name="login"),
    path('signup/', SignUp, name="signup" ),
    path('logoutUser/', LogoutUser, name="logout"),
    path('products/', Products, name="products"),
    path('productDetail/', ProductDetail, name="productDetail"),
    path('about/', About, name="about"),
    path('docs/', Documentation, name="docs"),
    path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),   
]