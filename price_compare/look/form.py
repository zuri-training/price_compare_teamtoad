
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import UserPlus




class CreateUserForm(UserCreationForm):
    class Meta:
        pass
        model = UserPlus
        fields = ["username","email","password1","password2"]