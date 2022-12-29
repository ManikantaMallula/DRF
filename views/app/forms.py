from django import forms

class Student(forms.Form):
    name=forms.CharField(max_length=40)
    rollno=forms.IntegerField()
    deptname=forms.CharField(max_length=40)