from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
    mobile_no=forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Mobile Number'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confrim Password'}))
    class Meta:
        model=User
        fields=['username','mobile_no','email','password1','password2']
