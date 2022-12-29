from django.core import validators
from django import forms
from .models import stu

class Student(forms.ModelForm):
    class Meta:
        model=stu
        fields=['name','age','password']
        labels={'name':'enter your name','age':'enter your age','password':'enter your password'}
        widgets={'password':forms.PasswordInput}