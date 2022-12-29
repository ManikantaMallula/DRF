from django import forms
from .models import modelDis


class formDis(forms.ModelForm):
    class Meta:
        model=modelDis
        fields=['name','age']
        label={'name':'NAME','age':'AGE'}



