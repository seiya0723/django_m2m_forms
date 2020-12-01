from django import forms 
from .models import Category,Allergy,Menu


class MenuForm(forms.ModelForm):
    class Meta:
        model   = Menu
        fields  = ["category","name","breakfast","lunch","dinner","takeout","price","allergy",]


