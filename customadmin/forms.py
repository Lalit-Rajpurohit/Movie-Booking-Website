from django import forms
from home.models import *


class MovieForm(forms.ModelForm):
    

    class Meta:
        model = Movie
        fields = '__all__'