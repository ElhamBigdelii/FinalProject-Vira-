from django import forms
from . import models

class Creatcharity(forms.ModelForm):
    class Meta:
        model=models.Charity
        fields=['name','address','sabt_number','description','web']
