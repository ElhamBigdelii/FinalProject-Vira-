from django import forms
from . import models

class Creatcharity(forms.ModelForm):
    class Meta:
        model=models.Charity
        fields=['name','address','sabt_number','description','web']


class addProject(forms.ModelForm):
    class Meta:
        model=models.Project
        fields=['title','cost' , 'description']
    
