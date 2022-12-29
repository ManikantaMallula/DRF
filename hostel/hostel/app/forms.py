
from django.core import validators
from app.models import hostel



from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class hostelform(forms.ModelForm):
    class Meta:
        model=hostel
        fields=['hname','cno','address']
        widgets={"hname":forms.TextInput(),
                 "cno":forms.TextInput(),
                 "address":forms.TextInput()


        }

class hostelform2(UserCreationForm):
    password2=forms.CharField(label='enter password again',widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email']




