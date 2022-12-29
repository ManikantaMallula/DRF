from django import forms
from django.forms.widgets import NumberInput

class Pat(forms.Form):

    fname=forms.CharField(min_length=7,max_length=20)
    lname=forms.CharField(min_length=7,max_length=20)
    Pno=forms.IntegerField()
    email=forms.EmailField()
    date=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

    doctors=[('1'," Dr.Alex"),('2',"Dr.John"),('3',"Dr.Siri"),('3',"Dr.Regina")]
    aa=[("1","Male"),("2","Female"),("3","Other")]

    Physicians= forms.CharField(label='Select Physician', widget=forms.RadioSelect(choices=doctors))
    Gender=forms.CharField(label='Gender', widget=forms.RadioSelect(choices=aa))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))




class Schol(forms.Form):
    Student_Name = forms.CharField(min_length=7, max_length=20)
    Father_Name = forms.CharField(min_length=7, max_length=20)
    bb=[("1","1st Year"),("2","2nd Year")]
    cc=[("1","MPC"),("1","CEC"),("1","MEC")]
    bb = [("1", "1st Year"), ("2", "2nd Year")]
    Cls = forms.ChoiceField(choices=bb)
    Cls = forms.ChoiceField(choices=cc)
    Aadhar_No=forms.IntegerField()
    Pan_No=forms.IntegerField()




gender=(('M','Male'),('F','Female'))
rate=(('q','1'),('w','2'),('e','3'),('f','4'),('e','5'))
class feedback(forms.Form):
    FirstName=forms.CharField(initial='enter your first name',strip=False,disabled=False,label_suffix="     ")
    LastName=forms.CharField(initial='enter your last name',strip=False,disabled=False,label_suffix="      ")
    phoneno=forms.IntegerField(initial="+91",widget=forms.PasswordInput)
    Email=forms.EmailField(help_text="must be@ and .com", required=False,label_suffix="   ")
    # Date=forms.DateField(widget=forms.selectDateField)
    Gender=forms.ChoiceField(choices=gender)
    feedback = forms.CharField(initial='', widget=forms.Textarea, help_text="Please share your feedback",error_messages=None)
    Rating = forms.CharField(widget=forms.RadioSelect(choices=rate))



class forth(forms.Form):
    first_name=forms.CharField(error_messages={'required':'please enter your name'})
    last_name=forms.CharField()
    Email_Address=forms.EmailField()
    Tittle=forms.CharField()
    phone=forms.IntegerField()
    cancel_registration=forms.ChoiceField(widget=forms.CheckboxInput)
    date=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    choi=[('1','campaignmanagement'),('2','CRMAdministration'),('3','EmailDeployment'),('4','Partner'),('5','Employee')]
    job_function=forms.CharField(label='JobFunction', widget=forms.RadioSelect(choices=choi))
    Dietery_Requirements=forms.CharField()
    Expectations=forms.CharField(widget=forms.Textarea)
