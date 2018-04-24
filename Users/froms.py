from django.contrib.auth.forms import UserCreationForm
from .models import Users

class RegisterForm(UserCreationForm):
    model = Users
    fileds = ('username','email','nickname')
