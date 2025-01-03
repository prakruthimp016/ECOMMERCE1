from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm,UserCreationForm
from django.contrib.auth.models import User

class identify(forms.Form):
    username=forms.CharField(max_length=100)

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


class EmailForm(forms.Form):
    to=forms.CharField(max_length=100)
    cc=forms.CharField(max_length=100,)
    sub=forms.CharField(max_length=100)
    body=forms.CharField(max_length=100,required=False)