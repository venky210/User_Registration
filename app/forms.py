from django import forms

from app.models import *

class userform(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}
        help_texts={'username':''}

class Profileform(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['address','profile_pic']
        

