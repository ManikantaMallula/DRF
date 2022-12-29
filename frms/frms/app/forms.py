from django import forms

class Stu(forms.Form):
    name=forms.CharField(max_length=20)
    age=forms.IntegerField(initial=16,help_text="enter your age")
    email=forms.EmailField(required=False)
  #  key=forms.CharField(widget=forms.HiddenInput())
  #  fff=forms.CharField(widget=forms.TextInput(attrs={'class': 'somecss1', 'id': 'uniqueid'}))
  #  password=forms.CharField(widget=forms.PasswordInput())

