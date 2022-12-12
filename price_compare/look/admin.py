from django.contrib import admin
from .models import  UserPlus
# Register your models here.

@admin.register(UserPlus)
class UserPlusAdmin(admin.ModelAdmin):
    list_display= ["first_name","id","facebook_url","twitter_url","email","username"]
