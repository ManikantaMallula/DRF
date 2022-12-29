
from django import forms

class StudentReg(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    age=forms.IntegerField(label='display_label')
    email=forms.EmailField()
    url=forms.URLField(required=False)
    float=forms.FloatField(required=False)
    image=forms.ImageField(required=False)
    date=forms.DateField(required=False)

class Employee(forms.Form):
    ename=forms.CharField()
    eid=forms.IntegerField()