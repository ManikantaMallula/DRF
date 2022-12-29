from django import forms

from django.core import validators

class stu(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()

        pwd=cleaned_data['password']
        rpwd=cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError("aaaaaaaaa")
         #   self.add_error('rpassword','wrong password')

