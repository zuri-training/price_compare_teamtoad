from django.contrib import admin
from .models import  *
# Register your models here.

@admin.register(UserPlus)
class UserPlusAdmin(admin.ModelAdmin):
    list_display= ["id","first_name","last_name","email","username"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display= ["id","product_name","url_kara", "url_konga", "url_jumia","image_url", "description", "created_at", "updated_at"]


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display= ["id","comments","customer_id","product_id","created_at","updated_at"]