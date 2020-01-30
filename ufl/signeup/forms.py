from django import forms
from users.models import Users

class Creatnewuser(forms.ModelForm):
    class Meta:
        model=Users
        fields = '__all__'
        exclude = ()